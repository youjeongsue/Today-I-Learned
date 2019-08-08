//문자열 반복

package bank_1946;

import java.util.Scanner;

public class p_2675{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for(int i=0;i<T;i++){
            int R = sc.nextInt();
            String S = sc.next();
            for(int j=0;j<S.length();j++){
                for(int k=0;k<R;k++)
                    System.out.print(S.charAt(j));
            }
            System.out.println();
        }
        sc.close();
	}
}