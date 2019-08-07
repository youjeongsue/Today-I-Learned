//평균

package bank_1946;

import java.util.Scanner;

public class p_1546 {
    public static double max(double scores[]) {
        double max = scores[0];
        for (int i = 0; i < scores.length; i++)
            if (scores[i] > max)
                max = scores[i];
        return max;
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int len = sc.nextInt();
        double[] scores = new double[len];
        for (int i = 0; i < len; i++) {
            scores[i] = sc.nextInt();
        }
        double max = max(scores);
        for (int i = 0; i < len; i++) {
            scores[i] = (scores[i] / max) * 100;
        }
        double sum = 0;
        for (int i = 0; i < len; i++) {
            sum += scores[i];
        }
        System.out.print(sum / len);
        sc.close();
    }
}