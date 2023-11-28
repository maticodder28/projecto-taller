package com.example.appviena;

import android.os.Parcel;
import android.os.Parcelable;

public class ProductoComanda implements Parcelable {
    private Producto producto;
    private int cantidad;

    public ProductoComanda(Producto producto, int cantidad) {
        this.producto = producto;
        this.cantidad = cantidad;
    }

    protected ProductoComanda(Parcel in) {
        producto = in.readParcelable(Producto.class.getClassLoader());
        cantidad = in.readInt();
    }

    @Override
    public void writeToParcel(Parcel dest, int flags) {
        dest.writeParcelable(producto, flags);
        dest.writeInt(cantidad);
    }

    @Override
    public int describeContents() {
        return 0;
    }

    public static final Creator<ProductoComanda> CREATOR = new Creator<ProductoComanda>() {
        @Override
        public ProductoComanda createFromParcel(Parcel in) {
            return new ProductoComanda(in);
        }

        @Override
        public ProductoComanda[] newArray(int size) {
            return new ProductoComanda[size];
        }
    };

    // Getters y setters
    public Producto getProducto() {
        return producto;
    }

    public void setProducto(Producto producto) {
        this.producto = producto;
    }

    public int getCantidad() {
        return cantidad;
    }

    public void setCantidad(int cantidad) {
        this.cantidad = cantidad;
    }
}
