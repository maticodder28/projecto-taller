package com.example.appviena;

import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class Login extends AppCompatActivity {

    private EditText etUsuario, etClave;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        etUsuario = findViewById(R.id.txtusuario);
        etClave = findViewById(R.id.txtclave);
        Button btnIngresar = findViewById(R.id.btnIngresar);

        btnIngresar.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                verificarCredenciales();
            }
        });
    }

    private void verificarCredenciales() {
        String email = etUsuario.getText().toString();
        String clave = etClave.getText().toString();

        ConexionDbHelper dbHelper = new ConexionDbHelper(Login.this);
        SQLiteDatabase db = dbHelper.getReadableDatabase();

        String[] projection = {
                ConexionDbHelper.COLUMN_ID,
                // Otros campos que necesites
        };

        String selection = "email" + " = ? AND " + "clave" + " = ?";
        String[] selectionArgs = { email, clave };

        Cursor cursor = db.query(
                ConexionDbHelper.TABLE_USERS,
                projection,
                selection,
                selectionArgs,
                null,
                null,
                null
        );

        if (cursor.moveToFirst()) {
            // Usuario encontrado, iniciar sesión
            cursor.close();
            db.close();
            iniciarSesion();
        } else {
            // Usuario no encontrado o contraseña incorrecta
            Toast.makeText(this, "Correo electrónico o contraseña incorrectos", Toast.LENGTH_SHORT).show();
            cursor.close();
            db.close();
        }
    }

    private void iniciarSesion() {
        // Aquí puedes iniciar tu Activity principal o lo que necesites hacer al iniciar sesión
        Intent intent = new Intent(Login.this, Menu.class);
        startActivity(intent);
        finish();
    }
}
