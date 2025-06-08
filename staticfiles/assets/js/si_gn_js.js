 const scrolls = document.querySelectorAll('.si_gn_input')
        const main = document.getElementById('si_gn_main')
        const cont = document.getElementById('si_gn_cont')
        
        let count = 0;
        scrolls.forEach((input) => {
            count += 1;
        })

        function durate() {
            var pageHeight = Math.max( document.body.scrollHeight, document.body.offsetHeight,
                           document.documentElement.clientHeight, document.documentElement.scrollHeight,
                           document.documentElement.offsetHeight );
            if (pageHeight > 500 || count < 5) {
            cont.id = 'si_gn_cont_op'
            main.id = 'si_gn_main_op'
        } else if(pageHeight < 600 && count > 4) {
            cont.id = 'si_gn_cont'
            main.id = 'si_gn_main'
        }
        console.log(pageHeight)
        }

        
        setInterval(durate, 5000)
        
        console.log(count)
        console.log(pageHeight)
        