package com.example.appviena;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

public class Menu extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_menu);

        // Botón para crear comanda
        findViewById(R.id.button).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Implementar la lógica para ir a la actividad de creación de comandas
                Intent intent = new Intent(Menu.this, CrearComanda.class);
                startActivity(intent);
            }
        });

        // Botón para listar comandas
        findViewById(R.id.button3).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Implementar la lógica para ir a la actividad que lista las comandas
                Intent intent = new Intent(Menu.this, ListadoComandas.class);
                startActivity(intent);
            }
        });

        // Botón para cerrar sesión
        findViewById(R.id.button4).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Implementar la lógica para cerrar la sesión del usuario
                // Esto podría incluir borrar la información de la sesión actual y volver al login
                Intent intent = new Intent(Menu.this, Login.class);
                intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TASK);
                startActivity(intent);
            }
        });

        // Botón para salir de la aplicación
        findViewById(R.id.button6).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Cierra la aplicación
                finishAffinity();
            }
        });
    }
}