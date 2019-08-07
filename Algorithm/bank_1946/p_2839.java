//설탕 배달
//나눗셈 -> 뺄셈으로 생각, break 꼭 걸어주기

package bank_1946;

import java.util.Scanner;

public class p_2839 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int count = 0;
        while (N > 0) {
            if (N % 5 == 0) {
                N -= 5;
                count++;
            } else if (N % 3 == 0) {
                N -= 3;
                count++;
            } else if (N > 5) {
                N -= 5;
                count++;
            } else {
                count = -1;
                break;
            }
        }
        System.out.print(count);
        sc.close();
    }
}