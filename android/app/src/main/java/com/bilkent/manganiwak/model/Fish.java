package com.bilkent.manganiwak.model;

public abstract class Fish extends GameObject {

    public Fish() {
        isControlledByAi = true;
        isControlledByKeyBoard = false;
        isControlledByMouse = false;
    }
}
