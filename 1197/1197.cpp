/*
 * MIT License
 * Copyright (c) 2018 yangyuan
 */
#include <cstdio>
#define STR_LEN 3

int main() {
    int N;
    char str[STR_LEN];
    while (scanf("%d", &N) != EOF) {
        for (int i = 0; i < N; i++) {
            scanf("%s", str);
            int h = str[0] - 'a' + 1;
            int v = str[1] - '0'; 
            if ((h == 1 || h == 8) || (v == 1 || v == 8)) {
                if ((h == v) || (h + v == 9)) {
                    printf("2\n");
                } else if ((h == 1 or h == 8) and (v == 2 || v == 7) ||
                        (v == 1 or v == 8) and (h == 2 || h == 7)) {
                    printf("3\n");
                } else {
                    printf("4\n");
                }
            } else if ((h == 2 || h == 7) || (v == 2 || v == 7)) {
                if ((h == v) || (h + v == 9)) {
                    printf("4\n");
                } else {
                    printf("6\n");
                }
            } else {
                printf("8\n");
            }
        }
    }
    return 0;
}
