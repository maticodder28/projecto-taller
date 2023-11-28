package com.example.appviena;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.TextView;

import java.text.SimpleDateFormat;
import java.util.List;
import java.util.Locale;

public class ComandaAdapter extends ArrayAdapter<Comanda> {
    public ComandaAdapter(Context context, List<Comanda> comandas) {
        super(context, 0, comandas);
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        Comanda comanda = getItem(position);
        if (convertView == null) {
            convertView = LayoutInflater.from(getContext()).inflate(R.layout.list_item_comanda, parent, false);
        }

        TextView tvFecha = convertView.findViewById(R.id.tvFecha);
        TextView tvTotal = convertView.findViewById(R.id.tvTotal);

        // Formatear la fecha para mostrarla en el TextView
        SimpleDateFormat dateFormat = new SimpleDateFormat("dd/MM/yyyy", Locale.getDefault());
        String fechaFormateada = dateFormat.format(comanda.getFecha());

        tvFecha.setText(fechaFormateada);
        tvTotal.setText(String.valueOf(comanda.getTotal()));

        return convertView;
    }
}