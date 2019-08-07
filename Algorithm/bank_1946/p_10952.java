//숫자의 합

package bank_1946;

import java.util.Scanner;

public class p_10952 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.next());
        String[] input = sc.next().split("");
        int sum = 0;
        for(int i=0;i<n;i++){
            sum+=Integer.parseInt(input[i]);
        }
        System.out.println(sum);
        sc.close();
    }
}