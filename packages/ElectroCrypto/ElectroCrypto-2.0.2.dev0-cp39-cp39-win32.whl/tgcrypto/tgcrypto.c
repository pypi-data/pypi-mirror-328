#define PY_SSIZE_T_CLEAN

#include <Python.h>

#include "aes256.h"
#include "ige256.h"
#include "ctr256.h"
#include "cbc256.h"

#define DESCRIPTION "Fast and Portable Cryptography Extension Library for Electrogram\n" \
    "TgCrypto is part of Electrogram, a Telegram MTProto library for Python\n" \
    "You can learn more about Electrogram here: https://Electrogram.org\n"

static PyObject *ige(PyObject *args, uint8_t encrypt) {
    Py_buffer data, key, iv;
    uint8_t *buf;
    PyObject *out;

    if (!PyArg_ParseTuple(args, "y*y*y*", &data, &key, &iv))    
        return NULL;    

    if (data.len == 0) {    
        PyErr_SetString(PyExc_ValueError, "Data must not be empty");    
        return NULL;    
    }    

    if (data.len % 16 != 0) {    
        PyErr_SetString(PyExc_ValueError, "Data size must match a multiple of 16 bytes");    
        return NULL;    
    }    

    if (key.len != 32) {    
        PyErr_SetString(PyExc_ValueError, "Key size must be exactly 32 bytes");    
        return NULL;    
    }    

    if (iv.len != 32) {    
        PyErr_SetString(PyExc_ValueError, "IV size must be exactly 32 bytes");    
        return NULL;    
    }    

    Py_BEGIN_ALLOW_THREADS    
        buf = ige256(data.buf, data.len, key.buf, iv.buf, encrypt);    
    Py_END_ALLOW_THREADS    

    PyBuffer_Release(&data);    
    PyBuffer_Release(&key);    
    PyBuffer_Release(&iv);    

    out = Py_BuildValue("y#", buf, data.len);    
    free(buf);    

    return out;
}

static PyObject *ige256_encrypt(PyObject *self, PyObject *args) {
    return ige(args, 1);
}

static PyObject *ige256_decrypt(PyObject *self, PyObject *args) {
    return ige(args, 0);
}

static PyObject *ctr256_encrypt(PyObject *self, PyObject *args) {
    Py_buffer data, key, iv, state;
    uint8_t *buf;
    PyObject *out;

    if (!PyArg_ParseTuple(args, "y*y*y*y*", &data, &key, &iv, &state))    
        return NULL;    

    if (data.len == 0) {    
        PyErr_SetString(PyExc_ValueError, "Data must not be empty");    
        return NULL;    
    }    

    if (key.len != 32) {    
        PyErr_SetString(PyExc_ValueError, "Key size must be exactly 32 bytes");    
        return NULL;    
    }    

    if (iv.len != 16) {    
        PyErr_SetString(PyExc_ValueError, "IV size must be exactly 16 bytes");    
        return NULL;    
    }    

    if (state.len != 1) {    
        PyErr_SetString(PyExc_ValueError, "State size must be exactly 1 byte");    
        return NULL;    
    }    

    if (*(uint8_t *) state.buf > 15) {    
        PyErr_SetString(PyExc_ValueError, "State value must be in the range [0, 15]");    
        return NULL;    
    }    

    Py_BEGIN_ALLOW_THREADS    
        buf = ctr256(data.buf, data.len, key.buf, iv.buf, state.buf);    
    Py_END_ALLOW_THREADS    

    PyBuffer_Release(&data);    
    PyBuffer_Release(&key);    
    PyBuffer_Release(&iv);    

    out = Py_BuildValue("y#", buf, data.len);    
    free(buf);    

    return out;
}

static PyObject *cbc(PyObject *args, uint8_t encrypt) {
    Py_buffer data, key, iv;
    uint8_t *buf;
    PyObject *out;

    if (!PyArg_ParseTuple(args, "y*y*y*", &data, &key, &iv))    
        return NULL;    

    if (data.len == 0) {    
        PyErr_SetString(PyExc_ValueError, "Data must not be empty");    
        return NULL;    
    }    

    if (data.len % 16 != 0) {    
        PyErr_SetString(PyExc_ValueError, "Data size must match a multiple of 16 bytes");    
        return NULL;    
    }    

    if (key.len != 32) {    
        PyErr_SetString(PyExc_ValueError, "Key size must be exactly 32 bytes");    
        return NULL;    
    }    

    if (iv.len != 16) {    
        PyErr_SetString(PyExc_ValueError, "IV size must be exactly 16 bytes");    
        return NULL;    
    }    

    Py_BEGIN_ALLOW_THREADS    
        buf = cbc256(data.buf, data.len, key.buf, iv.buf, encrypt);    
    Py_END_ALLOW_THREADS    

    PyBuffer_Release(&data);    
    PyBuffer_Release(&key);    
    PyBuffer_Release(&iv);    

    out = Py_BuildValue("y#", buf, data.len);    
    free(buf);    

    return out;
}

static PyObject *cbc256_encrypt(PyObject *self, PyObject *args) {
    return cbc(args, 1);
}

static PyObject *cbc256_decrypt(PyObject *self, PyObject *args) {
    return cbc(args, 0);
}

PyDoc_STRVAR(
    ige256_encrypt_docs,
    "ige256_encrypt(data, key, iv)\n"
    "--\n\n"
    "AES-256-IGE Encryption"
);

PyDoc_STRVAR(
    ige256_decrypt_docs,
    "ige256_decrypt(data, key, iv)\n"
    "--\n\n"
    "AES-256-IGE Decryption"
);

PyDoc_STRVAR(
    ctr256_encrypt_docs,
    "ctr256_encrypt(data, key, iv, state)\n"
    "--\n\n"
    "AES-256-CTR Encryption"
);

PyDoc_STRVAR(
    ctr256_decrypt_docs,
    "ctr256_decrypt(data, key, iv, state)\n"
    "--\n\n"
    "AES-256-CTR Decryption"
);

PyDoc_STRVAR(
    cbc256_encrypt_docs,
    "cbc256_encrypt(data, key, iv)\n"
    "--\n\n"
    "AES-256-CBC Encryption"
);

PyDoc_STRVAR(
    cbc256_decrypt_docs,
    "cbc256_decrypt(data, key, iv)\n"
    "--\n\n"
    "AES-256-CBC Encryption"
);

static PyMethodDef methods[] = {
    {"ige256_encrypt", (PyCFunction) ige256_encrypt, METH_VARARGS, ige256_encrypt_docs},
    {"ige256_decrypt", (PyCFunction) ige256_decrypt, METH_VARARGS, ige256_decrypt_docs},
    {"ctr256_encrypt", (PyCFunction) ctr256_encrypt, METH_VARARGS, ctr256_encrypt_docs},
    {"ctr256_decrypt", (PyCFunction) ctr256_encrypt, METH_VARARGS, ctr256_decrypt_docs},
    {"cbc256_encrypt", (PyCFunction) cbc256_encrypt, METH_VARARGS, cbc256_encrypt_docs},
    {"cbc256_decrypt", (PyCFunction) cbc256_decrypt, METH_VARARGS, cbc256_decrypt_docs},
    {NULL}
};

// Multi-phase initialization for free threading support
static PyModuleDef_Slot slots[] = {
    {Py_mod_exec, NULL},
    {0, NULL}
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    .m_name = "TgCrypto",
    .m_doc = DESCRIPTION,
    .m_size = 0,  // Using m_size = 0 for multi-phase initialization
    .m_methods = methods,
    .m_slots = slots
};

// Multi-phase module initialization function
PyMODINIT_FUNC PyInit_tgcrypto(void) {
    return PyModuleDef_Init(&module);
}