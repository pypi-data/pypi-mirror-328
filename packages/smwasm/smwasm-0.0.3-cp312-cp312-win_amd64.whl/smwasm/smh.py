import copy

from .smwasm import rs_load_wasm, rs_call, rs_register_native
from smwasm.core.smcore import g_funcs, g_paths, g_usages
from smwasm import smu


USAGE = "$usage"

_g_logger = None


def register(itdef, path, func):
    name = itdef[USAGE]
    g_usages[name] = itdef
    g_funcs[name] = func
    g_paths[name] = path


def load_wasm(wasm_path, page_num):
    rs_load_wasm(wasm_path, page_num)


def call(dt):
    usage = dt.get(USAGE)
    if usage in g_funcs:
        func = g_funcs.get(usage)
        dtRet = func(dt)
        return dtRet
    txt = rs_call(smu.dict_to_format_json(dt, 2))
    dtRet = smu.json_to_dict(txt)
    return dtRet


def call_in_text(intxt):
    dt = smu.json_to_dict(intxt)
    usage = dt.get(USAGE)
    if usage in g_funcs:
        func = g_funcs.get(usage)
        dtRet = func(dt)
        outtxt = smu.dict_to_format_json(dtRet, 2)
        return outtxt
    return '{}'


def info():
    ret = {"function": g_paths}
    return ret


def log(text):
    if _g_logger:
        _g_logger.info(text)
    else:
        print(text)


def register_native():
    rs_register_native()


def set_logger(logger):
    global _g_logger
    _g_logger = logger
