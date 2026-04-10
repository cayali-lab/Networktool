#include <stdio.h>
#include <string.h>

int validate_ip(char ip[]) {
    int a, b, c, d;
    char extra;

    if (sscanf(ip, "%d.%d.%d.%d%c", &a, &b, &c, &d, &extra) != 4) {
        return 0;
    }

    if (a < 0 || a > 255) return 0;
    if (b < 0 || b > 255) return 0;
    if (c < 0 || c > 255) return 0;
    if (d < 0 || d > 255) return 0;

    return 1;
}

int validate_port(int port) {
    return port >= 1 && port <= 65535;
}

int main() {
    int choice;
    char ip[100];
    int port;

    char log[100][100];   // log listesi
    int log_count = 0;

    while (1) {
        printf("\n= NÄTVERKSVERKTYG =\n");
        printf("1. Validera IP-adress\n");
        printf("2. Validera port\n");
        printf("3. Visa logg\n");
        printf("4. Avsluta\n");
        printf("Val: ");

        scanf("%d", &choice);

        if (choice == 1) {
            printf("Ange IP-adress: ");
            scanf("%s", ip);

            if (validate_ip(ip)) {
                printf("%s är en giltig IP-adress.\n", ip);
                sprintf(log[log_count++], "IP %s - giltig", ip);
            } else {
                printf("%s är inte en giltig IP-adress.\n", ip);
                sprintf(log[log_count++], "IP %s - ogiltig", ip);
            }

        } else if (choice == 2) {
            printf("Ange port: ");
            scanf("%d", &port);

            if (validate_port(port)) {
                printf("%d är en giltig port.\n", port);
                sprintf(log[log_count++], "Port %d - giltig", port);
            } else {
                printf("%d är inte en giltig port.\n", port);
                sprintf(log[log_count++], "Port %d - ogiltig", port);
            }

        } else if (choice == 3) {
            printf("\n= LOGG =\n");

            for (int i = 0; i < log_count; i++) {
                printf("%d. %s\n", i + 1, log[i]);
            }

        } else if (choice == 4) {
            printf("Totalt antal valideringar: %d\n", log_count);
            printf("Avslutar.\n");
            break;

        } else {
            printf("Ogiltigt val\n");
        }
    }

    return 0;
}
