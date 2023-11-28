package com.example.appviena;

import androidx.appcompat.app.AppCompatActivity;

import android.content.ContentValues;
import android.content.Intent;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.Locale;

public class CrearComanda extends AppCompatActivity {
    private ListView listViewProductos;
    private ProductoAdapter adapter;
    private ArrayList<Producto> productos;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_crear_comanda);

        listViewProductos = findViewById(R.id.listViewProductos);
        productos = cargarProductos();
        adapter = new ProductoAdapter(this, productos);
        listViewProductos.setAdapter(adapter);

        Button btnAgregarComanda = findViewById(R.id.buttonAgregarComanda);
        btnAgregarComanda.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                ArrayList<ProductoComanda> detallesComanda = new ArrayList<>();

                for (int i = 0; i < listViewProductos.getChildCount(); i++) {
                    View item = listViewProductos.getChildAt(i);
                    EditText etCantidad = item.findViewById(R.id.etCantidad);
                    int cantidad;

                    try {
                        cantidad = Integer.parseInt(etCantidad.getText().toString());
                    } catch (NumberFormatException e) {
                        cantidad = 0; // O manejar la excepción como prefieras
                    }

                    if (cantidad > 0) {
                        Producto producto = productos.get(i);
                        detallesComanda.add(new ProductoComanda(producto, cantidad));
                    }
                }

                if (!detallesComanda.isEmpty()) {
                    Intent intent = new Intent(CrearComanda.this, VerificarComandaActivity.class);
                    intent.putParcelableArrayListExtra("DETALLES_COMANDA", detallesComanda);
                    startActivity(intent);
                } else {
                    Toast.makeText(CrearComanda.this, "No se han seleccionado productos", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }


    private ArrayList<Producto> cargarProductos() {
        ArrayList<Producto> productos = new ArrayList<>();
        productos.add(new Producto(1, "Completo Italiano", "Pan, Vienesa, Tomate, Palta, Mayonesa Casera", 1500));
        productos.add(new Producto(2, "Coca Cola 350ml", "Bebida de fantasía sabor cola", 1000));
        // Añade aquí más productos según sea necesario
        return productos;
    }
    private String obtenerFechaActual() {
        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd", Locale.getDefault());
        return dateFormat.format(new Date());
    }
}



