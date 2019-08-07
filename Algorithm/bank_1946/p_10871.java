//X보다 작은 수

package bank_1946;

import java.util.Scanner;

public class p_10871 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int x = sc.nextInt();
        for(int i=0;i<n;i++){
            int num = sc.nextInt();
            if(num < x && i!=n-1){
                System.out.print(num+" ");
            }else if(num < x && i==n-1){
                System.out.print(num);
            }
        }
        sc.close();
    }
}