---
title: "C语言函数参考 — printf/scanf"
tags: [C, 函数参考, printf, scanf, stdio]
type: reference
created: 2026-05-27
---

# printf / scanf — 格式化输入输出

头文件：`#include <stdio.h>`

## printf — 输出到终端

```c
int printf(const char *format, ...);
```

| 格式符 | 含义 |
|--------|------|
| %d | 有符号十进制整数 |
| %u | 无符号十进制整数 |
| %f | 浮点数 |
| %c | 单个字符 |
| %s | 字符串 |
| %p | 指针地址 |
| %x | 十六进制 |
| %% | 打印 % 本身 |

示例：
```c
int a = 42;
float b = 3.14;
printf("a = %d, b = %.2f\n", a, b);
// 输出: a = 42, b = 3.14
```

返回值：成功输出时返回打印的字符数，失败返回负数。

## scanf — 从键盘读取输入

```c
int scanf(const char *format, ...);
```

注意：变量前要加 `&`（取地址）！

```c
int age;
float height;
char name[100];

scanf("%d", &age);          // 读整数
scanf("%f", &height);       // 读浮点数
scanf("%s", name);          // 读字符串（不加&）
```

返回值：成功匹配并赋值的项数。失败返回 EOF。
