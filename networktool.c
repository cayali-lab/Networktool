#include <stdio.h>

int main() {
    int choice;

    while (1) {
        printf("\n= NÄTVERKSVERKTYG =\n");
        printf("1. Validera IP-adress\n");
        printf("2. Validera port\n");
        printf("3. Visa logg\n");
        printf("4. Avsluta\n");
        printf("Val: ");

        scanf("%d", &choice);

        if (choice == 1) {
            printf("IP-validering kommer snart\n");
        } else if (choice == 2) {
            printf("Port-validering kommer snart\n");
        } else if (choice == 3) {
            printf("Logg kommer snart\n");
        } else if (choice == 4) {
            printf("Totalt antal valideringar: 0\n");
            printf("Avslutar.\n");
            break;
        } else {
            printf("Ogiltigt val\n");
        }
    }

    return 0;
}