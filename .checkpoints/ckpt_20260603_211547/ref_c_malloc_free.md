---
title: "C语言函数参考 — malloc/free"
tags: [C, 函数参考, malloc, free, 内存, stdlib]
type: reference
created: 2026-05-27
---

# malloc / free — 动态内存分配

头文件：`#include <stdlib.h>`

## malloc — 申请内存

```c
void *malloc(size_t size);
```

返回一个指向 `size` 字节内存的指针。失败返回 NULL。

```c
int *arr = malloc(10 * sizeof(int));  // 申请10个int的空间
if (arr == NULL) {
    printf("内存分配失败！\n");
    return 1;
}

arr[0] = 42;
arr[1] = 99;
// 使用完后释放
free(arr);
```

## free — 释放内存

```c
void free(void *ptr);
```

每次 malloc 都要配对 free。忘记释放 = 内存泄漏。

```c
int *p = malloc(100);
// ...使用p...
free(p);     // 释放
p = NULL;    // 好习惯：释放后置空
```

## calloc — 申请并清零

```c
void *calloc(size_t nmemb, size_t size);
```

申请 nmemb 个元素，每个 size 字节，自动初始化为 0。

```c
int *arr = calloc(10, sizeof(int));
// 10个元素全部初始化为0
```

## realloc — 重新调整大小

```c
void *realloc(void *ptr, size_t new_size);
```

```c
int *arr = malloc(5 * sizeof(int));
arr = realloc(arr, 10 * sizeof(int));  // 扩展到10个
```

## 常见错误

```c
int *p = malloc(100);
free(p);
free(p);   // 错误！double free

int *q = malloc(100);
// 忘记 free(q) → 内存泄漏
```
