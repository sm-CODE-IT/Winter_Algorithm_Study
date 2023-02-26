package week7.yejun;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _16563 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] nums = new int[N];
        for (int i=0; i<N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        for (int j=0; j<N; j++) {

            while (nums[j] != 1) {
                for (int i = 2; ; ) {
                    if (nums[j] == 1) break;

                    if (nums[j] % i == 0) {
                        sb.append(i).append(" ");
                        nums[j] /= i;
                    } else {
                        i++;
                    }
                }
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}
