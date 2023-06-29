package kr.co.aiai.app;

import android.content.Context;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import org.w3c.dom.Text;

import java.util.Random;

public class MainActivity9 extends AppCompatActivity {

    String com = "987";
    TextView tv;
    EditText et;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main9);

        et = findViewById(R.id.et);
        tv = findViewById(R.id.tv);
        Button btn = findViewById(R.id.btn);

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                myclick();
            }
        });
        ranC();

    }

    public void ranC() {
        String[] arr = {"1","2","3","4","5","6","7","8","9"};

        for (int i = 0; i < 100; i++) {
            int r = (int)(Math.random()*9);
            String a = arr[0];
            arr[0] = arr[r];
            arr[r] = a;
        }

        com = "" + arr[0] + arr[1] + arr[2];
        Log.d("soyeon", com);
    }

    public int getS(String mine, String com) {
        int ret = 0;
        String m1 = mine.substring(0,1);
        String m2 = mine.substring(1,2);
        String m3 = mine.substring(2,3);

        String c1 = com.substring(0,1);
        String c2 = com.substring(1,2);
        String c3 = com.substring(2,3);

        if(m1.equals(c1)) ret++;
        if(m2.equals(c2)) ret++;
        if(m3.equals(c3)) ret++;

        return ret;

    }

    public int getB(String mine, String com) {
        int ret = 0;
        String c1 = com.substring(0,1);
        String c2 = com.substring(1,2);
        String c3 = com.substring(2,3);

        String m1 = mine.substring(0,1);
        String m2 = mine.substring(1,2);
        String m3 = mine.substring(2,3);

        if(c1.equals(m2)||c1.equals(m3)) ret++;
        if(c2.equals(m1)||c2.equals(m3)) ret++;
        if(c3.equals(m1)||c3.equals(m2)) ret++;

        return ret;
    }

    public void myclick() {
        String mine = et.getText().toString();
        int s = getS(mine, com);
        int b = getB(mine,com);

        String str_old = tv.getText().toString();
        String str_new = mine+"   " + s+"s"+b+"b"+"\n";

        tv.setText(str_new + str_old);
        et.setText("");

        if(s==3) {
            Toast myToast = Toast.makeText(this.getApplicationContext(),"정답입니다!",Toast.LENGTH_SHORT);
            myToast.show();
        }

        Log.d("soyeon", mine+"   " + s+"s"+b+"b");

    }
}
