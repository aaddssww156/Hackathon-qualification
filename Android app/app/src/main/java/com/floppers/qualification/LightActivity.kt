package com.floppers.qualification

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.github.aachartmodel.aainfographics.aachartcreator.*
import com.github.aachartmodel.aainfographics.aaoptionsmodel.AAScrollablePlotArea
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext

class LightActivity : AppCompatActivity() {

    var timeList: MutableList<String> = mutableListOf()
    var dataList: MutableList<Any> = mutableListOf()
    var timeArray = Array<String>(100){""}
    var dataArray = Array<Any>(100){}

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_light)

        val retrofitApi = RetrofitHelper.getInstance().create(RetrofitApi::class.java)
        GlobalScope.launch {
            val res = retrofitApi.getLights()
            for (x in res.body()!!) {
                timeList.add(x.timedd)
                dataList.add(x.data)
            }

            for (x in 0 until timeList.size) timeArray[x] = timeList[x]
            for (x in 0 until dataList.size) dataArray[x] = dataList[x]

            withContext(Dispatchers.Main) {
                val chartView = findViewById<AAChartView>(R.id.chart)
                val chartModel: AAChartModel = AAChartModel()
                    .chartType(AAChartType.Column)
                    .title("Lights chart")
                    .subtitle("Today")
                    .backgroundColor("#ffffff")
                    .dataLabelsEnabled(true)
                    .categories(timeArray)
                    .zoomType(AAChartZoomType.XY)
                    .series(arrayOf(
                        AASeriesElement()
                            .name("brightnes %")
                            .data(dataArray)
                    ))
                chartModel.scrollablePlotArea = AAScrollablePlotArea()
                    .minWidth(10000)
                    .minHeight(100)
                    .opacity(150f)
                chartView.aa_drawChartWithChartModel(chartModel)
            }
        }
    }
}