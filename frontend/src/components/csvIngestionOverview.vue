<template>
  <div v-if="columnInfo" class="row">
    <!-- Main container row for the component -->
    <h2 align="center">Selected Column: {{ columnInfo.columnName }}</h2>

    <div class="row">
      <!-- First column with card displaying basic column info -->
      <div class="col-sm-12 col-md-6">
        <div class="card mt-3">
          <div class="card-header text-center grey">
                <h5>Overview</h5>
          </div>
          <div class="card-body">
            <div class="row">
              <div class="col-md-6 mt-3">
                <dt>Type:</dt>
                <dd>{{ columnInfo.columnType }}</dd>
              </div>
              <div class="col-md-6 mt-3">
                <dt>Length:</dt>
                <dd>{{ columnInfo.lenColumn }}</dd>
              </div>
            </div>
            <div class="row">
              <div class="col-md-6">
                <dt>Distinct Values:</dt>
                <dd>{{ columnInfo.distinctValues }}</dd>
              </div>
              <div class="col-md-6">
                <dt>Unique Values:</dt>
                <dd>{{ columnInfo.uniqueValues }}</dd>
              </div>
              <div class="col-md-6">
                <dt>Mean:</dt>
                <dd>{{ columnInfo.baseStats.meanColumn }}</dd>
              </div>
              <div class="col-md-6">
                <dt>Median:</dt>
                <dd>{{ columnInfo.baseStats.medianColumn }}</dd>
              </div>
            </div>
            <div class="row">
              <div class="col-md-6">
                <dt>Min:</dt>
                <dd>{{ columnInfo.baseStats.minColumn }}</dd>
              </div>
              <div class="col-md-6">
                <dt>Max:</dt>
                <dd>{{ columnInfo.baseStats.maxColumn }}</dd>
              </div>
            </div>
            <div v-if="'extraInfo' in columnInfo">
              <div class="row">
                <div class="col-md-6">
                  <dt>Numerical Rows:</dt>
                  <dd>{{ columnInfo.extraInfo.numberNumeric }}</dd>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Second column with pie chart and NaN Values -->
      <div class="col-sm-12 col-md-6">
        <basePieChart
          :values="[columnInfo.nanValues, 100 - columnInfo.nanValues]"
          :labels="['NanValues', 'Values']"
          :backgroundColor="['#5b5d62', '#fe5000']"
        ></basePieChart>
        <dt align="center">NaN Values:</dt>
        <dd align="center">{{ columnInfo.nanValues }}</dd>
      </div>

      <!-- Distribution images section -->
      <div v-if="'numericImages' in columnInfo">
        <div class="row pt-3">
          <h5 align="center">Distribution</h5>
          <div class="col-md-6">
            <div class="card">
              <div class="card-body">
                <dd align="center">
                  <img
                    v-bind:src="'data:image/jpeg;base64,' + columnInfo.numericImages.histogram"
                    alt="histogramImage"
                    class="img-fluid"
                  >
                </dd>
              </div>
            </div>
          </div>
          <div class="col-md-6">
            <div class="card">
              <div class="card-body">
                <dd align="center">
                  <img
                    v-bind:src="'data:image/jpeg;base64,' + columnInfo.numericImages.boxplot"
                    alt="boxplot"
                    class="img-fluid"
                  >
                </dd>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Data Patterns section -->
    <div v-if="'extraInfo' in columnInfo">
      <div class="col-md-12">
        <div class="card mt-3">
          <div class="card-header text-center grey" data-bs-toggle="tooltip" title="Show which patterns there are in your data. A represent a letter, 1 a number and & a special characters. The characters . , @ and / represent themself.">
            <h5>Data Patterns</h5>
          </div>
          <div class="card-body">
            <div class="row">
              <table class="table table-striped table-hover">
                <thead>
                  <tr>
                    <th scope="col">Pattern</th>
                    <th scope="col">Number of Rows</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(pattern, index) in columnInfo.extraInfo.patterns" :key="index">
                    <td>
                      {{ pattern[0] }}
                    </td>
                    <td>
                      {{ pattern[1] }}
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  
  </div>

    <!-- Data Preview section -->
    <div class="row pt-3">
      <div class="col-md-12">
        <div class="card mt-3">
          <div class="card-header text-center grey">
                <h5>Data Preview</h5>
          </div>
          <div class="card-body">
            <div class="row">
              <div class="col-md-12 overflow-auto">
                <div v-html="columnInfo.dataPreview"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import basePieChart from './basePieChart.vue';

export default {
  name: 'baseIngestionOverview',
  props: {
      columnInfo: Object
  },

  components:{
    basePieChart
  },

}       
    
</script>

