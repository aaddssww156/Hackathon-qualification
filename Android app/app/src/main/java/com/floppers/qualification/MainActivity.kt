package com.floppers.qualification

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val temperatureButton: Button = findViewById<Button>(R.id.TemperatureButton)
        val lightsButton: Button = findViewById<Button>(R.id.LightsButton)

        temperatureButton.setOnClickListener {
            val temperatureIntent: Intent = Intent(this, TemperatureActivity::class.java)
            startActivity(temperatureIntent)
        }

        lightsButton.setOnClickListener {
            val lightsIntent: Intent = Intent(this, LightActivity::class.java)
            startActivity(lightsIntent)
        }
    }
}