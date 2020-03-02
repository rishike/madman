 <template>
 <div id="dlgAttraction" class="modal is-clipped" :class="isActive">
    <div class="modal-background"> </div>
              <div id='form' class="modal-card is-7 is-offset-4">
                  <header class="modal-card-head">
                    <p class="modal-card-title"></p>
      <button class="delete btnCancel" aria-label="close" @click="hide()"></button>
    </header>
              <section class="modal-card-body">
                    <div class="field">
                          <div class="is-10 control">
                                <input type="text" class="input" id="name" placeholder="Attraction Name" v-model="name">
                                <p class="errors"></p>
                          </div>
                          <div class="is-2 control">
                                <span id="idDisplay" class="is-pulled-right"></span>
                          </div>
                    </div>
                          <div class="is-6 field">
                                <input type="text" class="input"  placeholder="Latitude" v-model="latVal">
                          </div>
                          <div class="is-6 field">
                                <input type="text" class="input" placeholder="Longitude" v-model="lngVal">
                          </div>
                    
                          <div class="is-6 field">
                                <select id="category" class="control" name="category" v-model="category">
                                    <option value="Park">Park</option>
                                    <option value="Museum">Museum</option>
                                    <option value="Place">Place</option>
                                    <option value="Neighborhood">Neighborhood</option>
                                    <option value="Pueblo Magico">Pueblo Magico</option>
                                    <option value="Temple">Temple</option>
                                </select>
                          </div>
                        

                         <div class="is-6 field">
                                <input type="text" class="input control" id="image" placeholder="Image File" name="image" v-model="image">
                          </div>
      
                    <div class="field">
                          <div class="is-12">
                                <input type="text" class="input control" id="weburl" placeholder="Web URL" name="weburl" v-model="weburl">
                          </div>
                    </div>
                </section>
                    <footer class="modal-card-foot">
                    <div id="addButtons" class="modal-card-foot">
                        <button id="btnClosest" class="button is-warning">Closest 5</button>
                        <button id="btnSave" class="button is-success" @click="save">Save</button>
                        <button class="button is-danger btnCancel" @click="hide()">Cancel</button>
                    </div>

                    <div id="editButtons" class="modal-card-foot">
                        <button id="btnUpdate" class="button is-success">Update</button>
                        <button id="btnDelete" class="button is-warning">Delete</button>
                        <button class="button is-danger btnCancel">Cancel</button>
                    </div>
                  </footer>

      
              <div id="table" class="modal-content is-7 is-offset-4">
                  <div id="tableData"></div>
              </div>

            </div>
        </div>
</template>
<script type="text/javascript">
  import axios from 'axios';
  export default {
    props:['isActive', 'latVal', 'lngVal'],
    data: function() {
      return {
        name:"",
        weburl:"",
        category:"",
        image:"",
        latitude:this.latitude,
        longitude:this.longitude
      }
    },
    methods:{
      hide: function() {
        this.$emit('isActiveEvt');
      },
      convertJsonToString: function(params) {
        let ret = "";
        for (let p of params) {
          ret = ret.concat(`${p}=${this.$data[p]}&`);

        }  
        return ret.replace(/[\&]$/g, "");
      },
      clearForm:function(params){
        for (let p of params){
            this.$data[p] = "";
        }
      },
      save: function() {
        const $this=this;
        axios({
        method: 'post',
        url: 'add_data/',
        data:this.convertJsonToString(["name","latitude", "longitude", "weburl","image","category"]),
        xsrfCookieName: 'csrftoken',
        xsrfHeaderName: 'X-CSRFToken',
        headers: {
                  'X-Requested-With': 'XMLHttpRequest',
                  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
                },
          }).then(function (response) { 
              if(response.data['success']) { 
                
                $this.hide();
                $this.clearForm(['name','weburl',
                      'category','image','latitude',
                      'longitude']);
              }
          }).catch(error => {

          }).finally(res => {

          });
      },
      getCookie: function (name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
          return cookieValue;
      }
    },
    created: function() {
      this.mapview = this.$parent;
    },
    watch: {
      latVal(newValue) {
        this.latitude = newValue;
      },
      lngVal(newValue) {
        this.longitude = newValue;
      }
    }
  };
</script>