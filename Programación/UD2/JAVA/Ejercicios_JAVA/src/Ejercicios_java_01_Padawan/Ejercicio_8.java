/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Ejercicios_java_01_Padawan;

/**
 * Alumno: Héctor Martín Ortega
 * 1º GS Desarrollo de Aplicaciones Multiplataforma
 * 
 * *************************ENUNCIADO*************************************
 * Ejercicio_8: Escribe un programa que pide la edad por teclado y 
 * nos muestra el mensaje de “Eres mayor de edad” solo si lo somos.
 * ***********************************************************************
 * 
 */
//Importamos el java.util.Scanner
import java.util.Scanner;
public class Ejercicio_8 {
    
    public static void main(String[] args){
        
        //Definimos las variables que vamos a usar
        int edad;
        
        //Declaro el objeto lector el cual es un scanner
        Scanner  lector= new Scanner(System.in);
    
        /**
         * Ahora muestro en pantalla el mensaje que dirá que se introduzca el 
         * valor para la edad.
         */
        
        System.out.println("Introduzca su edad: ");
        
        //Introducimos el aparatado de entrada de la distancia en millas
        edad = lector.nextInt();
        
        //introduciré las condiciones para resolver el ejercicio
        if (edad>=18)
        {
            //Muestro en pantalla el mensaje correspondiente a la solución.
            System.out.println("Eres mayor de edad.");
        }
    }
}
