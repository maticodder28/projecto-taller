package com.example.appviena;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.TextView;

import java.util.ArrayList;

public class ProductoAdapter extends ArrayAdapter<Producto> {
    public ProductoAdapter(Context context, ArrayList<Producto> productos) {
        super(context, 0, productos);
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        // Obtener el objeto Producto para esta posición
        Producto producto = getItem(position);

        // Verificar si una vista existente está siendo reutilizada, de lo contrario inflar la vista
        if (convertView == null) {
            convertView = LayoutInflater.from(getContext()).inflate(R.layout.list_item_producto, parent, false);
        }

        // Referencias a las vistas para setear los datos del producto
        TextView tvNombre = convertView.findViewById(R.id.tvNombreProducto);
        TextView tvPrecio = convertView.findViewById(R.id.tvPrecioProducto);
        EditText etCantidad = convertView.findViewById(R.id.etCantidad);

        // Llenar los datos
        tvNombre.setText(producto.getNombre());
        tvPrecio.setText(String.valueOf(producto.getPrecio()));
        etCantidad.setText(""); // Inicializar con vacío o un valor predeterminado

        // Devolver la vista completada para mostrarla en pantalla
        return convertView;
    }
}