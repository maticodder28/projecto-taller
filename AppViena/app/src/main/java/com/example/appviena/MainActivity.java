package com.example.appviena;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.view.WindowManager;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        this.getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN);

        new Handler().postDelayed(new Runnable() {
            @Override
            public void run() {
                // Cargamos el Activity principal
                Intent i = new Intent(MainActivity.this, Login.class);
                startActivity(i);
                // Cerramos el Activity Principal que en este caso es el MainActivity
                finish();
            }
        }, 5000); // Le damos el Tiempo de espera que esta en milisegundos
    }
}
