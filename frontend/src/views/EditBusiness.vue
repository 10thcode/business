<script setup>
  import { ref, onMounted } from 'vue';
  import { useRouter, useRoute } from 'vue-router'
  import Compressor from 'compressorjs';
  import PageTitle from '../components/PageTitle.vue';
  import IconButton from '../components/IconButton.vue';
  import Loading from "../components/Loading.vue";
  import { useAuth0 } from '@auth0/auth0-vue';


  const API_URL = import.meta.env.VITE_API_URL;
  const { user, isAuthenticated } = useAuth0();
  const loading = ref(true);
  const router = useRouter();
  const route = useRoute();
  const businessId = route.params.businessId;
  const business = ref({});
  const name = ref('');
  const category = ref('');
  const other_category = ref('');
  const short_description = ref('');
  const long_description = ref('');
  const address = ref('');
  const country_code = ref('');
  const phone = ref('');
  const email = ref('');
  const website = ref('');
  const image = ref(null);


  function handleMainImage (event) {
    const mainImage = event.target.files[0];

    if (mainImage) {
      new Compressor(mainImage, {
        quality: 0.4,
        success: (result) => {
          image.value = new File([result], result.name);
        },
        error: (err) => {
          throw new Error("Compression error");
        }
      });
    }
  }


  async function saveChanges () {
    loading.value = true;
    if (await isAuthenticated.value) {
      const formData = new FormData();

      formData.append('user_id', user.value.sub);
      formData.append('name', name.value);
      formData.append('category', category.value);
      formData.append('other_category', other_category.value);
      formData.append('short_description', short_description.value);
      formData.append('long_description', long_description.value);
      formData.append('address', address.value);
      formData.append('country_code', country_code.value);
      formData.append('phone', phone.value);
      formData.append('email', email.value);
      formData.append('website', website.value);
      if (image.value) {
        formData.append('image', image.value);
      }

      const response = await fetch(`${API_URL}/api/v1/businesses/${businessId}/`, {
        method: 'PUT',
        body: formData
      });

      if (!response.ok) {
        throw new Error("Server error");
      }

      const data = await response.json();

      router.push(`/businesses/${data.id}`);
    }
    loading.value = false;
  }


  onMounted(async () => {
    loading.value = true;
    const response = await fetch(`${API_URL}/api/v1/businesses/${businessId}`);

    if (!response.ok) {
      throw new Error("Server error");
    }

    business.value = await response.json();
    name.value = business.value.name;
    category.value = business.value.category;
    other_category.value = business.value.other_category;
    short_description.value = business.value.short_description;
    long_description.value = business.value.long_description;
    address.value = business.value.address;
    country_code.value = business.value.country_code;
    phone.value = business.value.phone;
    email.value = business.value.email;
    website.value = business.value.website;

    loading.value = false;
  });
</script>

<template>
  <Loading v-if="loading"/>
  <PageTitle>Edit business</PageTitle>
  <section class="form-container">
    <form @submit.prevent="saveChanges">
      <div class="field">
        <label for="name">Name *</label>
        <input
          required
          id="name"
          type="text"
          maxlength="60"
          placeholder="eg. Black Genius Company LTD"
          v-model="name"
        >
      </div>
      <div class="field">
        <label for="category">Category *</label>
        <select id="category" v-model="category" required>
          <option value="" disabled selected>Select category</option>
          <option value="Art">Art</option>
          <option value="Automotive">Automotive</option>
          <option value="Beauty">Beauty</option>
          <option value="Education">Education</option>
          <option value="Electronic">Electronic</option>
          <option value="Entertainment">Entertainment</option>
          <option value="Fashion">Fashion</option>
          <option value="Finance">Finance</option>
          <option value="Food">Food</option>
          <option value="Grocery">Grocery</option>
          <option value="Health">Health</option>
          <option value="Real Estate">Real Estate</option>
          <option value="Sport">Sport</option>
          <option value="Other">Other</option>
        </select>
      </div>
      <div class="field" v-if="category === 'Other'">
        <label for="other">Specify category *</label>
        <input
          required
          id="other"
          type="text"
          maxlength="60"
          placeholder="eg. Education"
          v-model="other_category"
        >
      </div>
      <div class="field">
        <label for="short_description">Short description *</label>
        <textarea
          required
          id="short_description"
          rows="3"
          maxlength="120"
          placeholder="eg. A cutting-edge technology company dedicated to developing software solutions ..."
          v-model="short_description"
        ></textarea>
      </div>
      <div class="field">
        <label for="long_description">Long description</label>
        <textarea
          id="long_description"
          rows="3"
          maxlength="360"
          placeholder="eg. We are at the forefront of digital revolution, specializing in the creation of advanced sofware solutions ..."
          v-model="long_description"
        ></textarea>
      </div>
      <div class="field">
        <label for="address">Address</label>
        <input
          id="address"
          type="text"
          maxlength="60"
          placeholder="eg. 221B Baker Street"
          v-model="address"
        >
      </div>
      <div class="field">
        <label for="country_code">Country code</label>
        <select id="country_code" v-model="country_code">
          <option value="" disabled selected>Select country code</option>
          <option value="93">Afghanistan (+93)</option>
          <option value="355">Albania (+355)</option>
          <option value="213">Algeria (+213)</option>
          <option value="376">Andorra (+376)</option>
          <option value="244">Angola (+244)</option>
          <option value="54">Argentina (+54)</option>
          <option value="374">Armenia (+374)</option>
          <option value="61">Australia (+61)</option>
          <option value="43">Austria (+43)</option>
          <option value="994">Azerbaijan (+994)</option>
          <option value="973">Bahrain (+973)</option>
          <option value="880">Bangladesh (+880)</option>
          <option value="375">Belarus (+375)</option>
          <option value="32">Belgium (+32)</option>
          <option value="501">Belize (+501)</option>
          <option value="229">Benin (+229)</option>
          <option value="975">Bhutan (+975)</option>
          <option value="591">Bolivia (+591)</option>
          <option value="387">Bosnia and Herzegovina (+387)</option>
          <option value="267">Botswana (+267)</option>
          <option value="55">Brazil (+55)</option>
          <option value="673">Brunei (+673)</option>
          <option value="359">Bulgaria (+359)</option>
          <option value="226">Burkina Faso (+226)</option>
          <option value="257">Burundi (+257)</option>
          <option value="855">Cambodia (+855)</option>
          <option value="237">Cameroon (+237)</option>
          <option value="1">Canada (+1)</option>
          <option value="238">Cape Verde (+238)</option>
          <option value="236">Central African Republic (+236)</option>
          <option value="235">Chad (+235)</option>
          <option value="56">Chile (+56)</option>
          <option value="86">China (+86)</option>
          <option value="57">Colombia (+57)</option>
          <option value="269">Comoros (+269)</option>
          <option value="243">Congo (+243)</option>
          <option value="682">Cook Islands (+682)</option>
          <option value="506">Costa Rica (+506)</option>
          <option value="385">Croatia (+385)</option>
          <option value="53">Cuba (+53)</option>
          <option value="357">Cyprus (+357)</option>
          <option value="420">Czech Republic (+420)</option>
          <option value="45">Denmark (+45)</option>
          <option value="253">Djibouti (+253)</option>
          <option value="1">Dominica (+1)</option>
          <option value="1">Dominican Republic (+1)</option>
          <option value="593">Ecuador (+593)</option>
          <option value="20">Egypt (+20)</option>
          <option value="503">El Salvador (+503)</option>
          <option value="240">Equatorial Guinea (+240)</option>
          <option value="291">Eritrea (+291)</option>
          <option value="372">Estonia (+372)</option>
          <option value="251">Ethiopia (+251)</option>
          <option value="679">Fiji (+679)</option>
          <option value="358">Finland (+358)</option>
          <option value="33">France (+33)</option>
          <option value="241">Gabon (+241)</option>
          <option value="220">Gambia (+220)</option>
          <option value="995">Georgia (+995)</option>
          <option value="49">Germany (+49)</option>
          <option value="233">Ghana (+233)</option>
          <option value="30">Greece (+30)</option>
          <option value="299">Greenland (+299)</option>
          <option value="1">Grenada (+1)</option>
          <option value="590">Guadeloupe (+590)</option>
          <option value="502">Guatemala (+502)</option>
          <option value="224">Guinea (+224)</option>
          <option value="245">Guinea-Bissau (+245)</option>
          <option value="592">Guyana (+592)</option>
          <option value="509">Haiti (+509)</option>
          <option value="504">Honduras (+504)</option>
          <option value="852">Hong Kong (+852)</option>
          <option value="36">Hungary (+36)</option>
          <option value="354">Iceland (+354)</option>
          <option value="91">India (+91)</option>
          <option value="62">Indonesia (+62)</option>
          <option value="98">Iran (+98)</option>
          <option value="964">Iraq (+964)</option>
          <option value="353">Ireland (+353)</option>
          <option value="972">Israel (+972)</option>
          <option value="39">Italy (+39)</option>
          <option value="225">Ivory Coast (+225)</option>
          <option value="876">Jamaica (+876)</option>
          <option value="81">Japan (+81)</option>
          <option value="962">Jordan (+962)</option>
          <option value="7">Kazakhstan (+7)</option>
          <option value="254">Kenya (+254)</option>
          <option value="686">Kiribati (+686)</option>
          <option value="383">Kosovo (+383)</option>
          <option value="965">Kuwait (+965)</option>
          <option value="996">Kyrgyzstan (+996)</option>
          <option value="856">Laos (+856)</option>
          <option value="371">Latvia (+371)</option>
          <option value="961">Lebanon (+961)</option>
          <option value="266">Lesotho (+266)</option>
          <option value="231">Liberia (+231)</option>
          <option value="218">Libya (+218)</option>
          <option value="423">Liechtenstein (+423)</option>
          <option value="370">Lithuania (+370)</option>
          <option value="352">Luxembourg (+352)</option>
          <option value="853">Macau (+853)</option>
          <option value="389">Macedonia (+389)</option>
          <option value="261">Madagascar (+261)</option>
          <option value="265">Malawi (+265)</option>
          <option value="60">Malaysia (+60)</option>
          <option value="960">Maldives (+960)</option>
          <option value="223">Mali (+223)</option>
          <option value="356">Malta (+356)</option>
          <option value="692">Marshall Islands (+692)</option>
          <option value="222">Mauritania (+222)</option>
          <option value="230">Mauritius (+230)</option>
          <option value="52">Mexico (+52)</option>
          <option value="691">Micronesia (+691)</option>
          <option value="373">Moldova (+373)</option>
          <option value="377">Monaco (+377)</option>
          <option value="976">Mongolia (+976)</option>
          <option value="382">Montenegro (+382)</option>
          <option value="212">Morocco (+212)</option>
          <option value="258">Mozambique (+258)</option>
          <option value="95">Myanmar (+95)</option>
          <option value="264">Namibia (+264)</option>
          <option value="674">Nauru (+674)</option>
          <option value="977">Nepal (+977)</option>
          <option value="31">Netherlands (+31)</option>
          <option value="687">New Caledonia (+687)</option>
          <option value="64">New Zealand (+64)</option>
          <option value="505">Nicaragua (+505)</option>
          <option value="227">Niger (+227)</option>
          <option value="234">Nigeria (+234)</option>
          <option value="683">Niue (+683)</option>
          <option value="850">North Korea (+850)</option>
          <option value="47">Norway (+47)</option>
          <option value="968">Oman (+968)</option>
          <option value="92">Pakistan (+92)</option>
          <option value="680">Palau (+680)</option>
          <option value="507">Panama (+507)</option>
          <option value="675">Papua New Guinea (+675)</option>
          <option value="595">Paraguay (+595)</option>
          <option value="51">Peru (+51)</option>
          <option value="63">Philippines (+63)</option>
          <option value="48">Poland (+48)</option>
          <option value="351">Portugal (+351)</option>
          <option value="974">Qatar (+974)</option>
          <option value="242">Republic of the Congo (+242)</option>
          <option value="40">Romania (+40)</option>
          <option value="7">Russia (+7)</option>
          <option value="250">Rwanda (+250)</option>
          <option value="590">Saint Barthélemy (+590)</option>
          <option value="290">Saint Helena (+290)</option>
          <option value="1">Saint Kitts and Nevis (+1)</option>
          <option value="1">Saint Lucia (+1)</option>
          <option value="590">Saint Martin (+590)</option>
          <option value="508">Saint Pierre and Miquelon (+508)</option>
          <option value="1">Saint Vincent and the Grenadines (+1)</option>
          <option value="685">Samoa (+685)</option>
          <option value="378">San Marino (+378)</option>
          <option value="239">São Tomé and Príncipe (+239)</option>
          <option value="966">Saudi Arabia (+966)</option>
          <option value="221">Senegal (+221)</option>
          <option value="381">Serbia (+381)</option>
          <option value="248">Seychelles (+248)</option>
          <option value="232">Sierra Leone (+232)</option>
          <option value="65">Singapore (+65)</option>
          <option value="421">Slovakia (+421)</option>
          <option value="386">Slovenia (+386)</option>
          <option value="677">Solomon Islands (+677)</option>
          <option value="252">Somalia (+252)</option>
          <option value="27">South Africa (+27)</option>
          <option value="82">South Korea (+82)</option>
          <option value="34">Spain (+34)</option>
          <option value="94">Sri Lanka (+94)</option>
          <option value="249">Sudan (+249)</option>
          <option value="597">Suriname (+597)</option>
          <option value="268">Swaziland (+268)</option>
          <option value="46">Sweden (+46)</option>
          <option value="41">Switzerland (+41)</option>
          <option value="963">Syria (+963)</option>
          <option value="886">Taiwan (+886)</option>
          <option value="992">Tajikistan (+992)</option>
          <option value="255">Tanzania (+255)</option>
          <option value="66">Thailand (+66)</option>
          <option value="228">Togo (+228)</option>
          <option value="690">Tokelau (+690)</option>
          <option value="676">Tonga (+676)</option>
          <option value="1">Trinidad and Tobago (+1)</option>
          <option value="216">Tunisia (+216)</option>
          <option value="90">Turkey (+90)</option>
          <option value="993">Turkmenistan (+993)</option>
          <option value="688">Tuvalu (+688)</option>
          <option value="256">Uganda (+256)</option>
          <option value="380">Ukraine (+380)</option>
          <option value="971">United Arab Emirates (+971)</option>
          <option value="44">United Kingdom (+44)</option>
          <option value="1">United States (+1)</option>
          <option value="598">Uruguay (+598)</option>
          <option value="998">Uzbekistan (+998)</option>
          <option value="678">Vanuatu (+678)</option>
          <option value="379">Vatican (+379)</option>
          <option value="58">Venezuela (+58)</option>
          <option value="84">Vietnam (+84)</option>
          <option value="681">Wallis and Futuna (+681)</option>
          <option value="212">Western Sahara (+212)</option>
          <option value="967">Yemen (+967)</option>
          <option value="260">Zambia (+260)</option>
          <option value="263">Zimbabwe (+263)</option>
        </select>
      </div>
      <div class="field">
        <label for="phone">Phone</label>
        <input
          id="phone"
          pattern="[0-9]{10}"
          maxlength="10"
          placeholder="eg. 0123456789"
          v-model="phone"
        >
      </div>
      <div class="field">
        <label for="email">Email</label>
        <input
          id="email"
          type="email"
          placeholder="eg. user@example.com"
          v-model="email"
        >
      </div>
      <div class="field">
        <label for="name">Website</label>
        <input
          id="name"
          type="url"
          placeholder="eg. https://www.example.com"
          v-model="website"
        >
      </div>
      <div class="field">
        <label for="main_image">Main image</label>
        <input
          type="file"
          id="main_image"
          accept="image/png, image/jpeg"
          @change="handleMainImage"
        >
      </div>
      <div class="form-buttons action-buttons">
        <IconButton @click="$router.push(`/businesses/${businessId}`)" color="accent" icon="close"/>
        <IconButton
          color="solid-accent"
          type="submit"
          icon="save">Save &nbsp</IconButton>
      </div>
    </form>
  </section>
</template>
