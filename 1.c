#include <stdio.h>
#include <string.h>

int main() {
    char s[] = "abcde";
    int n = strlen(s);
    for (int i = 0; i < n; i++) {
        printf("%s\n", s);
        char first = s[0];
        memmove(s, s + 1, n - 1);
        s[n - 1] = first;
    }
    return 0;
}
