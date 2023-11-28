package com.example.appviena;

import androidx.appcompat.app.AppCompatActivity;

import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.util.Log;
import android.widget.ListView;
import android.widget.TextView;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.Locale;

public class DetalleComandaActivity extends AppCompatActivity {
    private TextView tvFecha, tvTotal;
    private ListView lvProductos;
    private ProductoComandaAdapter adaptadorProductos;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detalle_comanda);

        tvFecha = findViewById(R.id.tvFechaComanda);
        tvTotal = findViewById(R.id.tvTotalComanda);
        lvProductos = findViewById(R.id.lvProductosComanda);

        int comandaId = getIntent().getIntExtra("COMANDA_ID", -1);
        if (comandaId != -1) {
            cargarDetalleComanda(comandaId);
        } else {
            // Manejar el caso en que el ID no se pase correctamente
        }
    }

    private void cargarDetalleComanda(long comandaId) {
        ConexionDbHelper dbHelper = new ConexionDbHelper(this);
        SQLiteDatabase db = dbHelper.getReadableDatabase();

        // Consultar la información básica de la comanda
        Cursor cursorComanda = db.query(
                ConexionDbHelper.TABLE_ORDERS,
                new String[] {ConexionDbHelper.COLUMN_FECHA, ConexionDbHelper.COLUMN_TOTAL},
                ConexionDbHelper.COLUMN_ID + "=?",
                new String[] {String.valueOf(comandaId)},
                null, null, null
        );

        if (cursorComanda.moveToFirst()) {
            String fecha = cursorComanda.getString(cursorComanda.getColumnIndex(ConexionDbHelper.COLUMN_FECHA));
            double total = cursorComanda.getDouble(cursorComanda.getColumnIndex(ConexionDbHelper.COLUMN_TOTAL));

            tvFecha.setText("Fecha: " + formatearFecha(fecha));
            tvTotal.setText("Total: $" + total);
        }
        cursorComanda.close();

        // Cargar los detalles de productos de la comanda
        ArrayList<ProductoComanda> detalles = obtenerDetallesComanda(comandaId);
        adaptadorProductos = new ProductoComandaAdapter(this, detalles);
        lvProductos.setAdapter(adaptadorProductos);

        db.close();
    }

    private ArrayList<ProductoComanda> obtenerDetallesComanda(long comandaId) {
        ArrayList<ProductoComanda> detalles = new ArrayList<>();
        ConexionDbHelper dbHelper = new ConexionDbHelper(this);
        SQLiteDatabase db = dbHelper.getReadableDatabase();

        // Realiza una consulta para obtener los detalles de la comanda específica
        Cursor cursor = db.query(
                ConexionDbHelper.TABLE_ORDER_DETAILS, // Nombre de la tabla de detalles de comanda
                new String[] {ConexionDbHelper.COLUMN_PRODUCTO_ID, ConexionDbHelper.COLUMN_CANTIDAD}, // Columnas a retornar
                ConexionDbHelper.COLUMN_COMANDA_ID + "=?", // Columnas para la cláusula WHERE
                new String[] {String.valueOf(comandaId)}, // Los valores para la cláusula WHERE
                null, null, null
        );

        try {
            while (cursor.moveToNext()) {
                int productoId = cursor.getInt(cursor.getColumnIndexOrThrow(ConexionDbHelper.COLUMN_PRODUCTO_ID));
                int cantidad = cursor.getInt(cursor.getColumnIndexOrThrow(ConexionDbHelper.COLUMN_CANTIDAD));

                // Obtiene el Producto por su ID
                Producto producto = obtenerProductoPorId(productoId, db);

                if (producto != null) {
                    detalles.add(new ProductoComanda(producto, cantidad));
                }
            }
        } finally {
            cursor.close();
        }

        db.close();
        return detalles;
    }

    private Producto obtenerProductoPorId(int productoId, SQLiteDatabase db) {
        // Definición de la consulta como ya la tienes
        Cursor cursor = db.query(
                ConexionDbHelper.TABLE_PRODUCTS,   // La tabla para consultar
                new String[] {ConexionDbHelper.COLUMN_ID, ConexionDbHelper.COLUMN_NAME,
                        ConexionDbHelper.COLUMN_DESCRIPTION, ConexionDbHelper.COLUMN_PRICE}, // Las columnas a retornar
                ConexionDbHelper.COLUMN_ID + " = ?", // Las columnas para la cláusula WHERE
                new String[] { String.valueOf(productoId) }, // Los valores para la cláusula WHERE
                null, null, null // No agrupar las filas, no filtrar por grupos de filas, no ordenar
        );

        // Debugging para imprimir los nombres de las columnas
        String[] columnNames = cursor.getColumnNames();
        for (String columnName : columnNames) {
            Log.d("DB_DEBUG", "Columna en DB: " + columnName);
        }

        // Procesamiento del Cursor para obtener el Producto
        Producto producto = null;
        if (cursor.moveToFirst()) {
            String nombre = cursor.getString(cursor.getColumnIndexOrThrow(ConexionDbHelper.COLUMN_NAME));
            String descripcion = cursor.getString(cursor.getColumnIndexOrThrow(ConexionDbHelper.COLUMN_DESCRIPTION));
            double precio = cursor.getDouble(cursor.getColumnIndexOrThrow(ConexionDbHelper.COLUMN_PRICE));

            producto = new Producto(productoId, nombre, descripcion, precio);
        }
        cursor.close();
        return producto;
    }



    private String formatearFecha(String fechaStr) {
        try {
            SimpleDateFormat formatoOriginal = new SimpleDateFormat("yyyy-MM-dd", Locale.getDefault());
            Date fecha = formatoOriginal.parse(fechaStr);
            SimpleDateFormat formatoNuevo = new SimpleDateFormat("dd-MM-yyyy", Locale.getDefault());
            return formatoNuevo.format(fecha);
        } catch (Exception e) {
            e.printStackTrace();
            return fechaStr; // Devuelve la fecha original en caso de error
        }
    }

    // Clase ProductoComandaAdapter y cualquier otra lógica necesaria...
}
