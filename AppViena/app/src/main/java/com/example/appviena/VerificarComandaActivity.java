package com.example.appviena;

import android.content.ContentValues;
import android.content.Intent;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.Locale;

public class VerificarComandaActivity extends AppCompatActivity {
    private ListView lvProductos;
    private TextView tvTotal;
    private ArrayList<ProductoComanda> detallesComanda;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_verificar_comanda);

        lvProductos = findViewById(R.id.lvVerificarProductos);
        tvTotal = findViewById(R.id.tvTotalVerificar);

        // Recibir los detalles de la comanda
        ArrayList<ProductoComanda> detallesComanda = (ArrayList<ProductoComanda>) getIntent().getSerializableExtra("DETALLES_COMANDA");

        // Calcula y muestra el total de la comanda
        double total = 0;
        for (ProductoComanda item : detallesComanda) {
            total += item.getProducto().getPrecio() * item.getCantidad();
        }
        tvTotal.setText("Total: $" + total);

        // Configurar y mostrar la lista de productos
        ProductoComandaAdapter adapter = new ProductoComandaAdapter(this, detallesComanda);
        lvProductos.setAdapter(adapter);

        // Botón para confirmar la comanda
        Button btnConfirmar = findViewById(R.id.btnConfirmarComanda);
        btnConfirmar.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                insertarComandaEnDB(detallesComanda);
                // Redirigir al usuario a otra pantalla o cerrar la actividad
                Intent intent = new Intent(VerificarComandaActivity.this, Menu.class);
                intent.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);
                startActivity(intent);
            }
        });

        // Botón para modificar la comanda
        Button btnModificar = findViewById(R.id.btnModificarComanda);
        btnModificar.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // Simplemente cierra esta actividad para volver a CrearComanda
                finish();
            }
        });
    }
    private void insertarComandaEnDB(ArrayList<ProductoComanda> detallesComanda) {
        ConexionDbHelper dbHelper = new ConexionDbHelper(this);
        SQLiteDatabase db = dbHelper.getWritableDatabase();

        double totalComanda = 0;
        for (ProductoComanda productoComanda : detallesComanda) {
            double precioProducto = productoComanda.getProducto().getPrecio();
            int cantidad = productoComanda.getCantidad();
            totalComanda += precioProducto * cantidad;
        }

        ContentValues comandaValues = new ContentValues();
        comandaValues.put(ConexionDbHelper.COLUMN_FECHA, obtenerFechaActual());
        comandaValues.put(ConexionDbHelper.COLUMN_TOTAL, totalComanda);

        long comandaId = db.insert(ConexionDbHelper.TABLE_ORDERS, null, comandaValues);

        if (comandaId == -1) {
            Toast.makeText(this, "Error al crear la comanda", Toast.LENGTH_SHORT).show();
            db.close();
            return;
        }

        for (ProductoComanda productoComanda : detallesComanda) {
            ContentValues detalleValues = new ContentValues();
            detalleValues.put(ConexionDbHelper.COLUMN_COMANDA_ID, comandaId);
            detalleValues.put(ConexionDbHelper.COLUMN_PRODUCTO_ID, productoComanda.getProducto().getId());
            detalleValues.put(ConexionDbHelper.COLUMN_CANTIDAD, productoComanda.getCantidad());

            db.insert(ConexionDbHelper.TABLE_ORDER_DETAILS, null, detalleValues);
        }

        db.close();
        Toast.makeText(this, "Comanda agregada exitosamente", Toast.LENGTH_SHORT).show();
    }

    private String obtenerFechaActual() {
        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd", Locale.getDefault());
        return dateFormat.format(new Date());
    }

}
