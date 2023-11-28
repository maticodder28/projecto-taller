package com.example.appviena;

import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ListView;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;

public class ListadoComandas extends AppCompatActivity {
    private ListView listViewComandas;
    private ComandaAdapter adapter;
    private ArrayList<Comanda> comandas;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_listado_comandas);

        listViewComandas = findViewById(R.id.listViewComandas);

        comandas = cargarComandas(); // Método para cargar comandas de la base de datos
        adapter = new ComandaAdapter(this, comandas);
        listViewComandas.setAdapter(adapter);

        listViewComandas.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                Comanda comandaSeleccionada = comandas.get(position);

                // Inicia DetalleComandaActivity y pasa el ID de la comanda como extra
                Intent intent = new Intent(ListadoComandas.this, DetalleComandaActivity.class);
                intent.putExtra("COMANDA_ID", comandaSeleccionada.getId());
                startActivity(intent);
            }
        });
    }

    private ArrayList<Comanda> cargarComandas() {
        ArrayList<Comanda> comandas = new ArrayList<>();
        ConexionDbHelper dbHelper = new ConexionDbHelper(this);
        SQLiteDatabase db = dbHelper.getReadableDatabase();

        // Define una proyección que especifica las columnas de la tabla que usarás
        String[] projection = {
                "id", // Ajusta estos nombres según tus definiciones de columna
                "usuario_id",
                "fecha",
                "total"
        };

        // Realiza una consulta para obtener los datos de las comandas
        Cursor cursor = db.query(
                "comandas", // Ajusta el nombre de la tabla según tu diseño
                projection, // Las columnas a retornar
                null,       // Las columnas para la cláusula WHERE
                null,       // Los valores para la cláusula WHERE
                null,       // No agrupar las filas
                null,       // No filtrar por grupos de filas
                null        // El orden de sort
        );

        try {
            while (cursor.moveToNext()) {
                int id = cursor.getInt(cursor.getColumnIndexOrThrow("id"));
                String fecha = cursor.getString(cursor.getColumnIndexOrThrow("fecha"));
                double total = cursor.getDouble(cursor.getColumnIndexOrThrow("total"));

                // Aquí debes ajustar según cómo estés manejando las fechas
                Date fechaDate = convertirStringADate(fecha); // Implementa este método según tu formato de fecha

                // Cargar detalles de la comanda (implementa este método según tu base de datos)
                ArrayList<ProductoComanda> detalles = obtenerDetallesComanda(id);

                Comanda comanda = new Comanda(id, fechaDate, total, detalles);
                comandas.add(comanda);
            }
        } finally {
            cursor.close();
        }

        return comandas;
    }

    private ArrayList<ProductoComanda> obtenerDetallesComanda(int comandaId) {
        ArrayList<ProductoComanda> detalles = new ArrayList<>();
        ConexionDbHelper dbHelper = new ConexionDbHelper(this);
        SQLiteDatabase db = dbHelper.getReadableDatabase();

        // Realiza una consulta para obtener los detalles de la comanda específica
        Cursor cursor = db.query(
                "detalles_comanda", // Nombre de la tabla de detalles de comanda
                new String[]{"producto_id", "cantidad"}, // Columnas a retornar
                "comanda_id = ?", // Columnas para la cláusula WHERE
                new String[]{String.valueOf(comandaId)}, // Los valores para la cláusula WHERE
                null, // groupBy
                null, // having
                null  // orderBy
        );

        try {
            while (cursor.moveToNext()) {
                int productoId = cursor.getInt(cursor.getColumnIndexOrThrow("producto_id"));
                int cantidad = cursor.getInt(cursor.getColumnIndexOrThrow("cantidad"));

                // Aquí se asume que tienes un método para obtener Producto por su ID
                Producto producto = obtenerProductoPorId(productoId);

                detalles.add(new ProductoComanda(producto, cantidad));
            }
        } finally {
            cursor.close();
        }

        return detalles;
    }

    private Date convertirStringADate(String fechaStr) {
        try {
            SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd");
            return format.parse(fechaStr);
        } catch (Exception e) {
            e.printStackTrace();
            return null; // O manejar de otra manera
        }
    }

    private Producto obtenerProductoPorId(int productoId) {
        ConexionDbHelper dbHelper = new ConexionDbHelper(this);
        SQLiteDatabase db = dbHelper.getReadableDatabase();

        // Define una proyección que especifica las columnas de la tabla que usarás
        String[] projection = {
                ConexionDbHelper.COLUMN_ID,
                ConexionDbHelper.COLUMN_NAME,
                ConexionDbHelper.COLUMN_DESCRIPTION,
                ConexionDbHelper.COLUMN_PRICE
        };

        // Filtrar resultados WHERE "id" = 'productoId'
        String selection = ConexionDbHelper.COLUMN_ID + " = ?";
        String[] selectionArgs = { String.valueOf(productoId) };

        Cursor cursor = db.query(
                ConexionDbHelper.TABLE_PRODUCTS,   // La tabla para consultar
                projection,       // Las columnas a retornar
                selection,        // Las columnas para la cláusula WHERE
                selectionArgs,    // Los valores para la cláusula WHERE
                null,             // No agrupar las filas
                null,             // No filtrar por grupos de filas
                null              // El orden de sort
        );

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

}


