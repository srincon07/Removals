(function() {
  var widget, initAddressFinder = function() {
      widget = new AddressFinder.Widget(
          document.getElementById('id_pickUp'),
          'ADDRESSFINDER_DEMO_KEY',
          'AU', {
              "address_params": {
                "gnaf" : "1"
              }
          }
      );
      widget.on('result:select', function(fullAddress, metaData) {
        // You will need to update these ids to match those in your form
        document.getElementById('id_pickUp').value = metaData.full_address;
      });
  };

  function downloadAddressFinder() {
      var script = document.createElement('script');
      script.src = 'https://api.addressfinder.io/assets/v3/widget.js';
      script.async = true;
      script.onload = initAddressFinder;
      document.body.appendChild(script);
  };

  document.addEventListener('DOMContentLoaded', downloadAddressFinder);
})();


(function() {
  var widget2, initAddressFinder2 = function() {
      widget2 = new AddressFinder.Widget(
          document.getElementById('id_dropOff'),
          'ADDRESSFINDER_DEMO_KEY',
          'AU', {
              "address_params": {
                "gnaf" : "1"
              }
          }
      );
      widget2.on('address:select', function(fullAddress, metaData2) {
        // You will need to update these ids to match those in your form
        document.getElementById('id_dropOff').value = metaData2.full_address;
      }); 
  };

  function downloadAddressFinder2() {
      var script = document.createElement('script');
      script.src = 'https://api.addressfinder.io/assets/v3/widget.js';
      script.async = true;
      script.onload = initAddressFinder2;
      document.body.appendChild(script);
  };

  document.addEventListener('DOMContentLoaded', downloadAddressFinder2);
})();