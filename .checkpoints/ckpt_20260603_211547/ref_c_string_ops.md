---
title: "C语言函数参考 — 字符串操作"
tags: [C, 函数参考, strlen, strcpy, strcmp, string]
type: reference
created: 2026-05-27
---

# 字符串操作函数

头文件：`#include <string.h>`

## strlen — 获取字符串长度

```c
size_t strlen(const char *s);
```

返回字符串长度，不包括结尾的 `\0`。

```c
char *s = "hello";
int len = strlen(s);  // len = 5
```

## strcpy / strncpy — 复制字符串

```c
char *strcpy(char *dest, const char *src);
char *strncpy(char *dest, const char *src, size_t n);
```

strcpy 不安全（不检查目标缓冲区大小）。优先用 strncpy。

```c
char dest[100];
strcpy(dest, "hello");          // dest = "hello"
strncpy(dest, "hello", 99);     // 最多复制99个字符，更安全
```

## strcmp — 比较字符串

```c
int strcmp(const char *s1, const char *s2);
```

| 返回值 | 含义 |
|--------|------|
| 0 | 两字符串相等 |
| < 0 | s1 < s2 |
| > 0 | s1 > s2 |

```c
if (strcmp(name, "admin") == 0) {
    printf("欢迎回来，管理员\n");
}
```

注意：不能直接用 `==` 比较字符串！那是比较指针地址。

## strcat — 拼接字符串

```c
char *strcat(char *dest, const char *src);
```

```c
char path[200] = "/home/user/";
strcat(path, "documents");  // path = "/home/user/documents"
```

## 安全建议

- 永远用 `strncpy` 替代 `strcpy`
- 永远用 `strncat` 替代 `strcat`
- C 字符串以 `\0` 结尾，忘记加会导致缓冲区溢出
