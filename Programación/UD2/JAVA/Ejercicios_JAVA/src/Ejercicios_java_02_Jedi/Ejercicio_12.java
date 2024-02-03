/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Ejercicios_java_02_Jedi;

/**
 * Alumno: Héctor Martín Ortega
 * 1º GS Desarrollo de Aplicaciones Multiplataforma
 * 
 * *************************ENUNCIADO*****************************************
 * Ejercicio_12:  Escribe un programa que lee un número y me dice si es 
 * positivo o negativo, consideraremos el cero como positivo.
 * ***************************************************************************
 */

//Importamos el java.util.Scanner
import  java.util.Scanner;

public class Ejercicio_12 {
    
    public static void main (String[] args){
        
        //Declaramos nuestras variables
        
        double num;
        
        //Introducimos lector y entrada como scanners.
         Scanner lector = new Scanner(System.in);
         
        
        /**
         * Mostramos en pantalla un mensaje para indicar que deberán de hacer.
         */
        
        System.out.println("Ahora deberá de el número correspondiente (puede"
                + "tener decimales");
        
        /**
         * Indicaré con un mensaje donde deberá de introducir el número del que
         * se desea conocer su signo
         */
        
        System.out.println("Introduzca  número: ");
        
        num = lector.nextDouble();
        
        /**
         * Ahora colocaremos el condicionante que nos dirá si el número es 
         * positivo o negativo, teniendo en cuenta que 0 será considerado 
         * positivo.
         */
        
        if (num >= 0) {
            System.out.println("Es positivo");
        } else {
            System.out.println("Es negativo");
        }
    }
}
