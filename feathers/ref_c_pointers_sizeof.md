---
title: "C语言函数参考 — 指针与 sizeof"
tags: [C, 函数参考, sizeof, 指针, 内存]
type: reference
created: 2026-05-27
---

# 指针与 sizeof

头文件：`#include <stddef.h>`（sizeof 是运算符，不是函数）

## sizeof — 获取类型/变量大小

```c
sizeof(type)
sizeof expression
```

返回 `size_t`（无符号整数），单位是字节。

```c
sizeof(char)     // 1
sizeof(int)      // 4（32位系统）
sizeof(double)   // 8
sizeof(int*)     // 8（64位系统）

int arr[10];
sizeof(arr)      // 40 = 10 * 4
sizeof(arr) / sizeof(arr[0])  // 10，数组元素个数
```

## 指针基础

```c
int a = 42;
int *p = &a;    // p 指向 a 的地址

*p = 99;        // 通过指针修改 a 的值
printf("%d", a);  // 输出 99
```

## 指针与数组

```c
int arr[5] = {10, 20, 30, 40, 50};
int *p = arr;     // 数组名 = 首元素地址

arr[0] == *p        // 相等
arr[1] == *(p+1)    // 相等
```

## 指针的 sizeof 陷阱

```c
int arr[10];
int *p = arr;

sizeof(arr)  // 40 — 整个数组的大小
sizeof(p)    // 8  — 指针本身的大小（64位系统）

// 传数组给函数时，数组会退化为指针！
void func(int arr[]) {
    sizeof(arr);  // 8，不是40！
}
```

## NULL 指针

```c
int *p = NULL;       // 指针不指向任何东西
if (p != NULL) {
    *p = 42;         // 安全：检查后才使用
}
```

## 常见错误

```c
int *p;
*p = 42;    // 错误！p没指向有效内存（野指针）

int *p = malloc(100);
free(p);
*p = 42;    // 错误！释放后继续使用（悬空指针）
```
