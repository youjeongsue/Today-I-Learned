//빠른 A+B

package bank_1946;

import java.io.*;
import java.util.StringTokenizer;

public class p_15552 {
    public static void main(String args[]) throws IOException {
        // 키보드 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());

            bw.write(A + B + "\n");
        }

        bw.flush();
        bw.close();
    }
}