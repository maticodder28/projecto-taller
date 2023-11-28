package com.example.appviena;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.TextView;

import java.util.ArrayList;

public class ProductoComandaAdapter extends ArrayAdapter<ProductoComanda> {
    private Context context;
    private ArrayList<ProductoComanda> listaProductos;

    public ProductoComandaAdapter(Context context, ArrayList<ProductoComanda> listaProductos) {
        super(context, 0, listaProductos);
        this.context = context;
        this.listaProductos = listaProductos;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        if (convertView == null) {
            convertView = LayoutInflater.from(context).inflate(R.layout.item_producto_comanda, parent, false);
        }

        ProductoComanda productoComanda = listaProductos.get(position);

        TextView tvNombreProducto = convertView.findViewById(R.id.tvNombreProducto);
        TextView tvCantidadProducto = convertView.findViewById(R.id.tvCantidadProducto);

        tvNombreProducto.setText(productoComanda.getProducto().getNombre());
        tvCantidadProducto.setText(String.valueOf(productoComanda.getCantidad()));

        return convertView;
    }
}
