package com.floppers.qualification

import retrofit2.Response
import retrofit2.http.GET

interface RetrofitApi {
    @GET("/data/?id_smartdevice=1")
    suspend fun getTemperature(): Response<List<TemperatureData>>

    @GET("/data/?id_smartdevice=2")
    suspend fun getLights(): Response<List<LightsData>>
}