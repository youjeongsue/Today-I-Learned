//날짜 계산

package bank_1946;

import java.util.Scanner;

public class p_1476 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int E = sc.nextInt();
        int S = sc.nextInt();
        int M = sc.nextInt();
        int e = 15, s = 28, m = 19, min;
        while (!(E == S && S == M && E == M)) {
            min = Math.min(Math.min(E, S), M);
            if (min == E)
                E += e;
            else if (min == S)
                S += s;
            else if (min == M)
                M += m;
        }
        System.out.println(E);
        sc.close();
    }
}