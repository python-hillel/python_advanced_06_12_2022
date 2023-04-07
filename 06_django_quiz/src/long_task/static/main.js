$(document).ready(() => {
   console.log('Status Check!');
});

$('.btn').on('click', function () {
    $.ajax({
        url: '/tasks/',
        data: { type: $(this).data('type') },
        method: 'POST',
    })
        .done((res) => {
            getStatus(res.task_id);
        })
        .fail((err) => {
            console.log(err);
        });
});

function getStatus(taskId) {
    $.ajax({
        url: `/tasks/${taskId}/`,
        method: 'GET'
    })
        .done((res) => {
            let html_status = ``;
            let html_result = ``;
            if (res.task_status === 'SUCCESS') {
                html_status = `<td style="color: green;">${res.task_status}</td>`
            } else if (res.task_status === 'PENDING') {
                html_status = `<td style="color: goldenrod;">${res.task_status}</td>`
            } else {
                html_status = `<td style="color: red;">${res.task_status}</td>`
            }

            if (res.task_result === 'True') {
                html_result = `<td style="font-weight: bold;">Done</td>`
            } else {
                html_result = `<td></td>`
            }

            const html = `
                <tr>
                    <td>${res.task_id}</td>
                    ${html_status}
                    ${html_result}
                </tr>`
            $('#tasks').prepend(html);

            // const taskStatus = res.task_status;

            if (res.task_status === 'SUCCESS' || res.task_status === 'FAILURE') return false;
            setTimeout(function () {
                getStatus(res.task_id);
            }, 1000);
        })
        .fail((err) => {
            console.log(err)
        });
}
