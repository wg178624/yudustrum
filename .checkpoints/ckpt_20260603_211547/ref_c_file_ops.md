---
title: "C语言函数参考 — 文件操作"
tags: [C, 函数参考, fopen, fclose, fread, fwrite, stdio]
type: reference
created: 2026-05-27
---

# 文件操作函数

头文件：`#include <stdio.h>`

## fopen — 打开文件

```c
FILE *fopen(const char *path, const char *mode);
```

| mode | 含义 |
|------|------|
| "r" | 只读 |
| "w" | 写入（清空文件） |
| "a" | 追加 |
| "r+" | 读写 |
| "rb" | 二进制只读 |
| "wb" | 二进制写入 |

```c
FILE *fp = fopen("data.txt", "r");
if (fp == NULL) {
    perror("打开文件失败");
    return 1;
}
```

## fclose — 关闭文件

```c
int fclose(FILE *fp);
```

每个 fopen 都要配对 fclose。

## fprintf / fscanf — 文件格式化读写

```c
fprintf(fp, "姓名: %s, 年龄: %d\n", name, age);
fscanf(fp, "%s %d", name, &age);
```

## fgets — 按行读取

```c
char *fgets(char *s, int size, FILE *stream);
```

```c
char line[256];
while (fgets(line, sizeof(line), fp)) {
    printf("读到了一行: %s", line);
}
```

## fread / fwrite — 二进制读写

```c
size_t fread(void *ptr, size_t size, size_t nmemb, FILE *stream);
size_t fwrite(const void *ptr, size_t size, size_t nmemb, FILE *stream);
```

```c
int data[10];
fread(data, sizeof(int), 10, fp);    // 读10个int
fwrite(data, sizeof(int), 10, fp);   // 写10个int
```

## 常用模式

```c
// 读文件标准模板
FILE *fp = fopen("file.txt", "r");
if (!fp) { perror("open"); return 1; }

char line[256];
while (fgets(line, sizeof(line), fp)) {
    // 处理每一行
    printf("%s", line);
}

fclose(fp);
```
