//평균은 넘겠지

package bank_1946;

import java.util.Scanner;

public class p_4344 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt(), sum;
        double mean, count;

        for (int i = 0; i < x; i++) {
            int y = sc.nextInt();
            int[] temp = new int[y];
            for (int j = 0; j < y; j++) {
                temp[j] = sc.nextInt();
            }
            sum = 0;
            for (int j = 0; j < y; j++) {
                sum += temp[j];
            }
            mean = sum / y;
            count = 0;
            for (int j = 0; j < y; j++) {
                if (temp[j] > mean)
                    count++;
            }
            System.out.println(String.format("%.3f", count / y * 100) + "%");
        }
        sc.close();
    }
}