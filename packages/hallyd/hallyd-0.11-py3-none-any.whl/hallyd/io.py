#  SPDX-FileCopyrightText: © 2021 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import abc
import contextlib
import json
import os
import subprocess
import threading
import time
import typing as t
import weakref

import hallyd.cleanup as _cleanup
import hallyd.fs as _fs
import hallyd.subprocess as _subprocess


@contextlib.contextmanager
def connect_diskimage(disk_image_path: "_fs.Path") -> t.ContextManager["_fs.Path"]:
    subprocess.check_output(["modprobe", "loop"])
    idev = 0
    while True:
        loop_dev_path = _fs.Path(f"/dev/loop{idev}")
        if not loop_dev_path.exists():
            break
        if subprocess.call(["losetup", "-P", loop_dev_path, disk_image_path]) == 0:
            cleanup = _cleanup.add_cleanup_task(_detach_loop_device, loop_dev_path,
                                                loop_device_by_dev_path(loop_dev_path).back_file)
            try:
                yield loop_dev_path
            finally:
                cleanup()
                while True:
                    if not subprocess.check_output(["losetup", "--associated", disk_image_path]).strip():
                        break
                    time.sleep(0.1)
            return
        idev += 1
    raise IOError("no free loop device available")


@contextlib.contextmanager
def connect_diskimage_buffered(dev_path: "_fs.Path", *, buffer_size_gb: float) -> t.ContextManager["_fs.Path"]:
    with _fs.temp_dir() as temp_dir:
        buffer_image_path = temp_dir("image")
        create_diskimage(buffer_image_path, size_gb=buffer_size_gb)
        try:
            with connect_diskimage(buffer_image_path) as buffer_device_path:
                yield buffer_device_path
            subprocess.check_output(["dd", f"if={buffer_image_path}", f"of={dev_path}", "bs=1M"])
        finally:
            buffer_image_path.unlink()


def create_diskimage(path: t.Union[str, "_fs.Path"], *, size_gb: float) -> None:
    subprocess.check_output(["dd", "if=/dev/zero", f"of={path}", "bs=1", "count=0", f"seek={int(size_gb*1024**3)}"])


def all_loop_devices():
    # noinspection SpellCheckingInspection
    return [_LoopDevice(**kwargs) for kwargs in json.loads(subprocess.check_output(["losetup", "-Jl"]))["loopdevices"]]


def loop_device_by_dev_path(dev_path: "_fs.Path") -> t.Optional["_LoopDevice"]:
    for loop_device in all_loop_devices():
        if loop_device.dev_path == dev_path:
            return loop_device


_locks = {}
_locks_lock = threading.Lock()


def lock(lock_path: "_fs.TInputPath", *, is_reentrant: bool = True, peek_interval: float = 0.25) -> "Lock":
    def weakcheck(p):
        with _locks_lock:
            x = _locks.get(p)
            if x and not x():
                _locks.pop(p)
    lock_path = _fs.Path(lock_path).resolve()
    with _locks_lock:
        result_weakref = _locks.get(str(lock_path))
        result = result_weakref() if result_weakref else None
        if not result:
            result = lock = _Lock(lock_path, is_reentrant, peek_interval)
            _locks[str(lock_path)] = weakref.ref(lock)
            weakref.finalize(lock, lambda: weakcheck(str(lock_path)))
        return result


class Lock(abc.ABC):

    def __enter__(self):
        self.acquire()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.release()

    @abc.abstractmethod
    def acquire(self, blocking: bool = True, timeout: float = -1) -> bool:
        pass

    @abc.abstractmethod
    def release(self) -> None:
        pass

    @abc.abstractmethod
    def locked(self) -> bool:
        pass


class _Lock(Lock):

    def __init__(self, lock_path: "_fs.Path", is_reentrant: bool, peek_interval: float):
        self.__lock_path = lock_path
        self.__locked_count = 0
        self.__locked_by_thread = None
        self.__is_reentrant = is_reentrant
        self.__peek_interval = peek_interval

    def acquire(self, blocking=True, timeout=-1):
        if not (self.__is_reentrant and self.__locked_by_thread == threading.get_native_id()):
            timeout_at = None if (timeout < 0) else (time.monotonic() + timeout)
            next_lock_alive_check_at = 0
            self.__lock_path.parent.make_dir(until=_fs.Path("/TODO/.."), exist_ok=True, preserve_perms=True, readable_by_all=True)
            while True:
                try:
                    self.__lock_path.make_file(exist_ok=False, readable_by_all=True)
                    self.__lock_path.write_text(json.dumps(_subprocess.process_permanent_id_for_pid(os.getpid())))
                    break
                except FileExistsError:
                    if next_lock_alive_check_at <= time.monotonic():
                        next_lock_alive_check_at = time.monotonic() + 10
                        try:
                            lock_process_permanent_id = json.loads(self.__lock_path.read_text())
                        except (FileNotFoundError, json.JSONDecodeError):
                            continue
                        if _subprocess.is_process_running(lock_process_permanent_id) is False:
                            self.__lock_path.unlink(missing_ok=True)
                            continue
                    if (not blocking) or (timeout_at and (timeout_at < time.monotonic())):
                        return False
                    time.sleep(self.__peek_interval)
        self.__locked_count += 1
        self.__locked_by_thread = threading.get_native_id()
        return True

    def release(self):
        if not self.locked():
            raise RuntimeError("release an unlocked Lock is forbidden")
        self.__locked_count -= 1
        if self.__locked_count == 0:
            self.__lock_path.unlink()
            self.__locked_count = False
            self.__locked_by_thread = None

    def locked(self):
        return self.__locked_count > 0


def _detach_loop_device(dev_path, back_file):
    loop_device = loop_device_by_dev_path(dev_path)
    if loop_device and loop_device.back_file == back_file:
        loop_device.detach()


class _LoopDevice:

    def __init__(self, **kwargs):
        self.__dev_path = _fs.Path(kwargs["name"])
        self.__back_file = _fs.Path(kwargs["back-file"])

    @property
    def dev_path(self) -> "_fs.Path":
        return self.__dev_path

    @property
    def back_file(self) -> "_fs.Path":
        return self.__back_file

    def detach(self):
        subprocess.check_output(["losetup", "-d", self.dev_path], stderr=subprocess.STDOUT)
