from ctypes.wintypes import *
import ctypes

LONG_PTR = LPARAM
HCURSOR = HANDLE
LRESULT = ctypes.c_long
SIZE_T = ctypes.c_size_t
FARPROC = ctypes.CFUNCTYPE(ctypes.c_int, LPVOID)
LPTHREAD_START_ROUTINE = ctypes.CFUNCTYPE(DWORD, LPVOID)
WNDPROC = ctypes.WINFUNCTYPE(LRESULT, HWND, UINT, WPARAM, LPARAM)
WNDENUMPROC = ctypes.WINFUNCTYPE(BOOL, HWND, LPARAM)
PFNLVCOMPARE = ctypes.WINFUNCTYPE(ctypes.c_int, LPARAM, LPARAM, LPARAM)
