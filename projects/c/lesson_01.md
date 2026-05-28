# C 语言学习 — 第 1 课：跑起来再说

## 你的第一个 C 程序

创建一个文件 `hello.c`：

```c
#include <stdio.h>

int main(void)
{
    printf("Hello, 王刚！\n");
    return 0;
}
```

## 编译和运行

```bash
gcc hello.c -o hello
./hello
```

## 这段代码告诉你三件事

| 行 | 作用 | 后续会细讲 |
|:---|:-----|:----------|
| `#include <stdio.h>` | 引入标准输入输出库 | 预处理指令 |
| `int main(void)` | 程序入口，C 程序从这里开始执行 | 函数 |
| `printf(...)` | 输出文字到终端 | 字符串 + 格式化输出 |
| `return 0;` | 告诉系统"程序正常结束" | 返回值 |

## 作业

1. 把 "Hello, 王刚！" 改成你的英文名 "Hello, gang！"
2. 再加一行 `printf` 输出你正在学 C 的感受
3. 编译运行，看结果
