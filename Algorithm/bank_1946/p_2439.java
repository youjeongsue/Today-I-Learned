//별 찍기 - 2

package bank_1946;

import java.util.Scanner;

public class p_2439{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        for(int i=1;i<=N;i++){
            for(int j=0;j<(N-i);j++){
                System.out.print(" ");
            }
            for(int k=0;k<i;k++){
                System.out.print("*");
            }
            System.out.println();
        }
        sc.close();
	}
}