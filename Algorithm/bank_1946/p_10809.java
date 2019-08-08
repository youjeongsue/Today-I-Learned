//알파벳 찾기

package bank_1946;

import java.util.Scanner;

public class p_10809{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        for(int i=0;i<25;i++){
            System.out.print(s.indexOf((char)(i+97))+" ");
        }
        System.out.print(s.indexOf((char)(122)));
        sc.close();
	}
}