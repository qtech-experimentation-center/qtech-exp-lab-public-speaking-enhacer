package com.example.heartbeatreader;

import android.os.Bundle;
import android.support.wearable.activity.WearableActivity;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.TextView;

public class MainActivity extends WearableActivity {

    private TextView mTextView;
    private Button btnStartReader;
    private boolean readerActivated = false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mTextView = findViewById(R.id.textView);
        btnStartReader = findViewById(R.id.btnStartReader);

        btnStartReader.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                if(readerActivated == false) {
                    mTextView.setText("Activated");
                    readerActivated = true;
                }
                else {
                    mTextView.setText("Desactivated");
                    readerActivated = false;
                }

            }
        });

        // Enables Always-on
        setAmbientEnabled();
    }
}
