# -*- coding: utf-8 -*-

import msgpack

'''
# 1. 一次性打包解包 (常规数据类型)，使用 packb 和 unpack (别名 dumps 和 loads )
list1 = [1, 2, 3, 4]
print(list1)
pack1 = msgpack.packb(list1)
print(pack1)
unpack1 = msgpack.unpackb(pack1)
print(unpack1)
# * 将 列表 解包为 元组
unpack2 = msgpack.unpackb(pack1,use_list=False)
print(unpack2)
'''

'''
# 2. 流解包 （ BytesIO类型 ）（将 多个包 一次解包到一个 unpacker 对象）
from io import BytesIO
buf = BytesIO()
for i in range(100):
    # print(range(i))
    buf.write(msgpack.packb(list(range(i))))
buf.seek(0)
# 注：此处不能使用msgpack.unpackb(buf)，否则报类型错误，TypeError: a bytes-like object is required, not '_io.BytesIO'
unpacker = msgpack.Unpacker(buf)
for unpacked in unpacker:
    print(unpacked)
'''

'''
# 3. 打包 自定义数据类型 temp：2017.03.03，未测试通过
import datetime

useful_dict = {
    "id": 1,
    "created": datetime.datetime.now(),
}


def decode_datetime(obj):
    if b'__datetime__' in obj:
        obj = datetime.datetime.strptime(obj["as_str"], "%Y%m%dT%H:%M:%S.%f")
    return obj


def encode_datetime(obj):
    if isinstance(obj, datetime.datetime):
        return {'__datetime__': True, 'as_str': obj.strftime("%Y%m%dT%H:%M:%S.%f")}
    return obj

print(useful_dict)
packed_dict = msgpack.packb(useful_dict, default=encode_datetime)
this_dict_again = msgpack.unpackb(packed_dict, object_hook=decode_datetime)
print(this_dict_again)
'''


# ext type 用法示例
import msgpack
packed = msgpack.packb(msgpack.ExtType(42, b'xyzzy'))
up = msgpack.unpackb(packed)
print(up)


# 4. 扩展类型 temp
import array


def default(obj):
    if isinstance(obj, array.array) and obj.typecode == 'd':
        return msgpack.ExtType(42, obj.tostring())
    raise TypeError("Unknown type: %r" % (obj,))


def ext_hook(code, data):
    if code == 42:
        a = array.array('d')
        a.fromstring(data)
        return a
    return msgpack.ExtType(code, data)

data = array.array('d', [1.2, 3.4])
packed = msgpack.packb(data, default=default)
unpacked = msgpack.unpackb(packed, ext_hook=ext_hook)
print(data == unpacked)




# 5. 先进的解包控制 temp

from io import BytesIO

def distribute(unpacker, get_worker):
    nelems = unpacker.read_map_header()
    for i in range(nelems):
        # Select a worker for the given key
        key = unpacker.unpack()
        worker = get_worker(key)

        # Send the value as a packed message to worker
        bytestream = BytesIO()
        unpacker.skip(bytestream.write)
        worker.send(bytestream.getvalue())
