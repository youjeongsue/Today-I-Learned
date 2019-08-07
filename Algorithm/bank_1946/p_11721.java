//열 개씩 끊어 출력하기

package bank_1946;

import java.util.Scanner;

public class p_11721 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        String input = sc.next();
        for (int i = 0; i < input.length(); i += 10) {
            int end = (i + 10 < input.length()) ? i + 10 : input.length();
            System.out.println(input.substring(i, end));
        }
        sc.close();
    }
}

/*
 * public static void main(String args[]){ System.out.println(new
 * Scanner(System.in).next().replaceAll("(.{10})","$1\n")); }
 */