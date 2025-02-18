#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import abc
import datetime
import functools
import json
import math
import os
import string
import threading
import time
import typing as t

import hallyd.bindle as _bindle


_T = t.TypeVar("_T", bound=object)


def call_now_with_retry(*, tries: int = 8, interval: float = 30, interval_fact: float = 1,
                        retry_on: t.Optional[t.Iterable[type[Exception]]] = None) -> t.Callable:  # TODO use
    def decorator(fct, *args, **kwargs):
        return with_retry(tries=tries, interval=interval, interval_fact=interval_fact,
                          retry_on=retry_on)(fct)(*args, **kwargs)
    return decorator


def with_retry(*, tries: int = 8, interval: float = 30, interval_fact: float = 1,
               retry_on: t.Optional[t.Iterable[type[Exception]]] = None) -> t.Callable:
    if retry_on is None:
        retry_on = [Exception]
    def decorator(fct):
        @functools.wraps(fct)
        def func(*a, **b):
            nwi = interval
            for itr in reversed(range(tries)):
                try:
                    return fct(*a, **b)
                except Exception as e:
                    if (itr > 0) and any((issubclass(type(e), x) for x in retry_on)):
                    #    import krrezzeedtest.log
                     #   krrezzeedtest.log.debug(traceback.format_exc(), tag="grayerror")
                        time.sleep(nwi)
                        nwi *= interval_fact
                    else:
                        raise
        return func
    return decorator


def with_friendly_repr_implementation(*, skip: t.Iterable[str] = ()):
    #  TODO test (for all classes that use it);   more reliable (cycles?!)
    return functools.partial(_with_friendly_repr_implementation__decorator, tuple(skip))


def _with_friendly_repr_implementation__decorator(skip_, cls_):
    def friendly_repr(self):
        objdict = json.loads(_bindle.dumps(self))
        module_name, type_name = objdict.pop(_bindle._TYPE_KEY)
        objdict = _bindle._filter_unneeded_dict_entries(type(self), objdict)
        objdict = {key: value for key, value in objdict.items() if key not in skip_}
        params_pieces = []
        for key, value in objdict.items():
            params_pieces.append(f"{key}={repr(value)}")
        full_type_name = (f"{module_name}." if module_name else "") + type_name
        return f"{full_type_name}({', '.join(params_pieces)})"

    cls_.__repr__ = friendly_repr
    return cls_


class Counter:

    def __init__(self):
        self.__current = 0
        self.__lock = threading.Lock()

    def next(self):
        with self.__lock:
            self.__current += 1
            return self.__current


_unique_id_counter = Counter()

_unique_id_sources = [(time.time_ns, datetime.datetime(9999, 1, 1, 0, 0, 0).timestamp() * 1000**3),
                      (_unique_id_counter.next, 99999),
                      (threading.get_native_id, 2**32-1),
                      (functools.partial(os.getpgid, 0), 2**32-1)]


def unique_id(*, numeric_only: bool = False) -> str:
    alphabet = string.digits if numeric_only else f"{string.digits}{string.ascii_uppercase}{string.ascii_lowercase}"
    alphabet_len = len(alphabet)
    result = ""
    for source, range_max in _unique_id_sources:
        number = source()
        result_piece = ""
        while number > 0:
            result_piece = alphabet[number % alphabet_len] + result_piece
            number = number // alphabet_len
        length = math.floor(math.log(range_max, alphabet_len)) + 1
        result += result_piece[-length:].rjust(length, alphabet[0])
    return result


def execute_in_parallel(funcs: list[t.Callable[[], None]]) -> None:
    threads = [_ExecuteParallelThread(func) for func in funcs]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    errors = [thread.error for thread in threads if thread.error]
    if errors:
        errors_text = ", ".join([str(e) for e in errors])
        raise Exception(f"TODO Error(s) in parallel execution: {errors_text}")


class _ExecuteParallelThread(threading.Thread):

    def __init__(self, fct: t.Callable[[], None]):
        super().__init__(daemon=True)
        self.__fct = fct
        self.error = None

    def run(self):
#            with self.__logsection:
        try:
            self.__fct()
        except Exception as e:
            self.error = e


class _AllAbstractMethodsProvidedByTrickMeta(abc.ABCMeta, t.Generic[_T]):

    def __new__(mcs, name, bases, namespace):
        x = type.__new__(mcs, name, bases, namespace)
        for foo in [xx for xx in dir(_T) if not xx.startswith("_")]:
            setattr(x, foo, None)
        return x


class AllAbstractMethodsProvidedByTrick(t.Generic[_T], metaclass=_AllAbstractMethodsProvidedByTrickMeta[_T]):
    pass
