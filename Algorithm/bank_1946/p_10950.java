//A+B - 3

package bank_1946;

import java.util.Scanner;

public class p_10950{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for(int i=0;i<T;i++){
            System.out.println(sc.nextInt()+sc.nextInt());
        }
        sc.close();
	}
}