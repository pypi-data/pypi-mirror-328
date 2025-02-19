//ROADMAP: use typescript and compile using Vite (+ include gettext compilation in Vite process)
/**
 * @file Automatically added to the HTML document (in layout.html).
 */

const NOW = new Date()

/**
 * Indicate whether we're running in DEBUG mode.
 * @type {boolean}
 */
const DEBUG = document.body.dataset.debug == 'true'

/**
 * Base URL for the website (with trailing slash).
 * @type {string}
 */
const SITE_PREFIX = document.body.dataset.scriptPrefix

/**
 * Base path for static files (with trailing slash).
 * @type {string}
 */
const STATIC_PREFIX = document.body.dataset.staticPrefix

/**
 * Base path for media files (with trailing slash).
 * @type {string}
 */
const MEDIA_PREFIX = document.body.dataset.mediaPrefix

/**
 * Base URL for the websockets (with trailing slash).
 */
const WEBSOCKET_PREFIX = SITE_PREFIX.replace('https://', 'wss://').replace('http://', 'ws://')

const LANG = document.documentElement.lang

const U18N_MESSAGES = {
    'fr': {
        ":": " :",
        "Connection to web server closed": "Connexion au serveur interrompue",
        "Unauthorized": "Non autorisé",
        "Celery broker is not connected": "le broker Celery n'est pas connecté",
        "Try to reconnect": "Essayer de se reconnecter",
        "There are more results": "Il y a des résultats supplémentaires",
    },
    'ru': {
        ":": ":",
        "Connection to web server closed": "Соединение с веб-сервером закрыто",
        "Unauthorized": "Несанкционированный",
        "Celery broker is not connected": "Celery брокер не подключен",
        "Try to reconnect": "Попробуйте переподключиться",
        "There are more results": "Есть еще результаты",
    },
}

/**
 * Bootstrap layout breakpoints.
 * 
 * See https://getbootstrap.com/docs/5.0/layout/breakpoints/
 */
const breakpoint = {
    xs: 0,
    sm: 576,
    md: 768,
    lg: 992,
    xl: 1200,
    xxl: 1400,
}

const formatters = {
    int(value) {
        if (value === undefined || value === null || value === '')
            return value

        return parseInt(value).toLocaleString()
    },

    boolCheck(value) {
        if (value === "True" || value === true) {
            return `<i class="bi-check"></i>`
        }
        else if (value === "False" || value === false) {
            return ''
        }
        else {
            return value
        }
    },

    date(value) {
        if (!value) {
            return value
        }
    
        const date = new Date(value)
        const localeStr = date.toLocaleString()
    
        const pos = localeStr.indexOf(' ')
        if (pos <= 0) {
            return localeStr
        }
    
        if (value.length == 10) { // value is assumed to be given as a date
            return localeStr.substring(0, pos)
        }
    
        if (localStorage.getItem('settings-fulldate') == '1') {
            return localeStr
        }
    
        if (isToday(date)) {
            return `<span title="${localeStr}">${localeStr.substring(pos + 1)}</span>`
        }
        else {
            return `<span title="${localeStr}">${localeStr.substring(0, pos)}</span>`
        }
    },

    link(value, row) {
        if (! value || ! row._data.link) {
            return value
        }
        
        return `<a href="${row._data.link}">${value}</a>`
    },

    following(value, row, index, field) {
        if (typeof(field) != 'number') {
            console.error(`cannot use following formatter with non-numeric field: ${field}`)
            return value
        }
        const following = row[field+1]
        if (! following) {
            return following
        }
        return following.replace(/{value}/g, value)
    },
}
// Put formatters in the global scope so that bootstrapTables can use them in HTML
window.formatters = formatters

const taskFormatters = {
    shortId: function (value) {
        if (! value) {
            return value
        }
        let base = window.location.pathname.replace(/\/$/, '')
        return `<a href="${base}/${value}/" title="${value}">${value.substring(0,8)}…</a>`
    },

    state: function (value) {
        let color = 'secondary'
        switch (value) {
            case 'STARTED': color = 'primary'; break
            case 'PROGRESS': color = 'info'; break
            case 'FAILURE': color = 'danger'; break
            case 'SUCCESS': color = 'success'; break
            case 'RETRY': color = 'warning'; break
            case 'ISSUE': color = 'warning'; break
        }
        return `<span class="text-${color}">${value}</span>`
    },

    progress: function (value, row) {
        if (value === null || value === undefined) {
            return null
        }
    
        value = parseInt(value)
        return `<div class="progress"><div class="progress-bar${row['state'] == 'PROGRESS' ? ' progress-bar-striped progress-bar-animated' : ''}" role="progressbar" aria-valuenow="${value}%" aria-valuemin="0" aria-valuemax="100" style="width: ${value}%">${value}%</div></div>`
    },

    duration: function (value, row) {
        return `<span class='task-duration' data-task-id="${row.id}">${calculateDuration(row.start, row.end) ?? '-'}</span>`
    },
}
window.taskFormatters = taskFormatters

const sorters = {
    numeric(fieldA, fieldB) {
        const aa = parseFloat(fieldA)
        const bb = parseFloat(fieldB)
        if (aa < bb) {
            return -1
        }
        if (aa > bb) {
            return 1
        }
        return 0
    }
}
window.sorters = sorters

class MessageManager {
    constructor() {
        this._container = document.getElementById('messages') // in layout.html
        this._fixedAfter = parseInt(document.body.dataset.messagesFixedAfter ?? 75)
        this._content = document.getElementById('messages-content')
        this._closeAll = document.getElementById('messages-close-all')
    
        this._closeAll.querySelector('a').addEventListener('click', ev => {
            ev.preventDefault()
            this.clear()
        })

        new MutationObserver(this._onUpdate).observe(this._content, {childList: true})
        this._onUpdate()
    }

    /**
     * Add a message with the given level.
     * @param {string} level
     * @param {string} html
     */
    add(level, html) {
        let color = 'primary'
        if (level) {
            switch (level.toUpperCase()) {
                case 'DEBUG': color = 'secondary'; break
                case 'INFO': color = 'info'; break
                case 'SUCCESS': color = 'success'; break
                case 'WARNING': color = 'warning'; break
                case 'ERROR': color = 'danger'; break
            }
        }
    
        // Create message element
        /** @type {HTMLDivElement} */
        let elem = fromHTML(`<div class="alert alert-${color} alert-dismissible fade show" role="alert">${html}<button type="button" class="btn-close" data-bs-dismiss="alert"></button></div>`)
        this._content.appendChild(elem)

        // Fix the messages container at the top of the screen if scrolling above `_fixedAfter`.
        // See CSS class `fixed-messages` defined in `base.css`.
        if (this._fixedAfter > 0) {
            if (window.scrollY > this._fixedAfter) {
                this._container.classList.add('fixed-messages')
            }
        }

        return elem
    }
    
    /**
     * Remove all messages.
     */
    clear() {
        while (this._content.firstChild) {
            this._content.removeChild(this._content.lastChild)
        }

        if (this._closeAll) {
            this._closeAll.classList.add('d-none')
        }
    }

    /**
     * Add a message with the `DEBUG` level.
     * @param {string} html
     * @returns {HTMLDivElement} The `div` element containing the message.
     */
    debug(html) {
        return this.add('DEBUG', html)
    }

    /**
     * Add a message with the `INFO` level.
     * @param {string} html
     * @returns {HTMLDivElement} The `div` element containing the message.
     */
    info(html) {
        return this.add('INFO', html)
    }

    /**
     * Add a message with the `SUCCESS` level.
     * @param {string} html
     * @returns {HTMLDivElement} The `div` element containing the message.
     */
    success(html) {
        return this.add('SUCCESS', html)
    }

    /**
     * Add a message with the `WARNING` level.
     * @param {string} html
     * @returns {HTMLDivElement} The `div` element containing the message.
     */
    warning(html) {
        return this.add('WARNING', html)
    }

    /**
     * Add a message with the `ERROR` level.
     * @param {string} html
     * @returns {HTMLDivElement} The `div` element containing the message.
     */
    error(html) {
        return this.add('ERROR', html)
    }
    
    /**
     * Display a `Dismiss all` button if several messages appear.
     */
    _onUpdate() {
        if (this._content.childElementCount >= 2) {
            this._closeAll.classList.remove('d-none')
        }
        else {
            this._closeAll.classList.add('d-none')
            
            if (this._fixedAfter > 0) {
                if (this._content.childElementCount == 0) {
                    this._container.classList.remove('fixed-messages')
                }
            }
        }
    }
}

const messages = new MessageManager()

function gettext(msg, ...args) {
    const translations = U18N_MESSAGES[LANG]
    msg = translations ? (translations[msg] ?? msg) : msg
    if (args.length > 0) {
        msg = msg.format(...args)
    }
    return msg
}

/**
 * Create element(s) in the DOM from its HTML representation.
 * 
 * See https://stackoverflow.com/a/35385518
 * 
 * @param {String} html
 * @return {Element | HTMLCollection} The created DOM element(s).
 */
function fromHTML(html) {
    const template = document.createElement('template')
    template.innerHTML = html
    const result = template.content.children
    if (result.length == 1)
        return result[0]
    return result
}

/**
 * @param {Date} date 
 * @returns {boolean}
 */
function isToday(date) {
    if (! date) {
        return false
    }
    
    return date.getDate() == NOW.getDate() && date.getMonth() == NOW.getMonth() && date.getFullYear() == NOW.getFullYear()
}

/**
 * @param {HTMLElement} titleElem 
 * @returns 
 */
function initShowHide(titleElem) {
    const content = document.getElementById(titleElem.dataset.showhide)
    if (! content) {
        console.error(`showhide content with id "${titleElem.dataset.showhide}" not found`)
        return
    }

    const icon = fromHTML(`<i></i>`)
    const button = fromHTML(`<a href="#" class="ms-2 text-dark"></a>`)
    button.appendChild(icon)
    titleElem.appendChild(button)

    function updateButton(hidden) {
        localStorage.setItem(`showhide-${titleElem.dataset.showhide}-hidden`, hidden ? '1' : '0')
        if (hidden) {
            icon.className = 'bi-toggle-off'
            button.title = "Show"
        }
        else {
            icon.className = 'bi-toggle-on'
            button.title = "Hide"
        }
    }

    let hidden
    const savedHidden = localStorage.getItem(`showhide-${titleElem.dataset.showhide}-hidden`)
    if (savedHidden) {
        hidden = savedHidden == '1'
        if (hidden) {
            content.classList.add('d-none')
        }
        else {
            content.classList.remove('d-none')
        }
    }
    else {
        hidden = content.classList.contains('d-none')
    }

    updateButton(hidden)
    button.addEventListener('click', ev => {
        updateButton(content.classList.toggle('d-none'))
        ev.preventDefault()
    })
}

/**
 * Submit a form, displaying a loading icon in the submit while the request is ongoing.
 * 
 * @param {HTMLFormElement} form The form to submit.
 * @param {object} options
 * @param {object} options.data Data to add to the default data (FormData if method is post, QueryString if method is get) .
 * @param {string} options.url URL to use (instead of form action).
 * @param {boolean} options.json Parse content as JSON.
 * @param {boolean} options.successMessage Display content as a success message.
 * @param {{(content: string): void}} options.onSuccess Success callback.
 */
function submitLoading(form, {data, url, json, successMessage, onSuccess} = {}) {
    const formData = new FormData(form)
    if (data) {
        for (const key in data) {
            formData.set(key, data[key])
        }
    }

    if (! url) {
        url = form.getAttribute('action')
    }

    let init
    if (form.method == 'post') {
        init = { method: 'post', body: formData }
    }
    else {
        const params = new URLSearchParams(formData)
        url += `?${params}`
        init = { method: 'get' }
    }

    const submitButton = form.querySelector('button[type="submit"]')
    const submitButtonHTML = submitButton.innerHTML
    
    // Disable button and display loading state
    submitButton.innerHTML = `<span class="spinner-border spinner-border-sm" aria-hidden="true"></span><span class="visually-hidden" role="status">Loading...</span>`
    submitButton.disabled = true

    fetch(url, init).then(res => {
        const contentPromise = json ? res.json() : res.text()
        contentPromise.then(content => {
            if (successMessage) {
                messages.add(res.ok ? 'SUCCESS' : 'ERROR', content)
            }
            if (onSuccess && res.ok) {
                onSuccess(content)
            }
        })
        .catch(err => messages.error(err))
    }).catch(err => {
        messages.error(err)
    }).finally(() => {        
        // Re-enable button
        submitButton.innerHTML = submitButtonHTML
        submitButton.disabled = false
    })
}

/**
 * Initialize a bootstrap table from the given tableId, using the default configuration.
 * 
 * @param {string} tableId  ID of the table.
 * @param {object} opts
 * @param {{[field: string]: object}} opts.fields  Column configurations for field names (require `th` elements to have `data-field` attributes).
 * @param {string} opts.sortName   Name of the sort field to use by default: `name` if not specified.
 * @param {string} opts.sortOrder  Order of the sort to use by default (`asc` or `desc`): `asc` if not specified.
 * @param {number} opts.pageSize   Number of items in a page by default: 25 if not specified.
 * @param {Array<object>} opts.columns  Column configurations in the order of `th` elements.
 * @param {object} opts.options  Other options.  
 */
function initTable(tableId, {fields, sortName, sortOrder, pageSize, columns, ...options} = {}) {
    const table = document.getElementById(tableId)
    table.classList.add('table', 'table-sm', 'table-bordered')

    if (options.pagination === undefined) {
        options.pagination = true
    }

    if (options.search === undefined) {
        options.search = true
    }

    if (options.toolbar === undefined) {
        options.toolbar = `#${tableId}-toolbar`
    }

    function parseIntIfNumeric(value) {
        // sortName is an integer if column option 'field' was not provided
        if (value === null) {
            return null
        }
        return value.match(/^\d+$/) ? parseInt(value) : value
    }

    options.sortName = parseIntIfNumeric(localStorage.getItem(`bt-${tableId}-sortName`)) ?? sortName
    options.sortOrder = localStorage.getItem(`bt-${tableId}-sortOrder`) ?? (sortOrder ?? 'asc')
    options.onSort = (name, order) => {
        localStorage.setItem(`bt-${tableId}-sortName`, name)
        localStorage.setItem(`bt-${tableId}-sortOrder`, order)
    }

    options.pageSize = localStorage.getItem(`bt-${tableId}-pageSize`) ?? pageSize ?? 25
    options.onPageChange = (number, size) => {
        localStorage.setItem(`bt-${tableId}-pageSize`, size)
    }

    if (columns === undefined) {
        columns = []
    }

    // Ensure there is a column for each <th>, and retrieve field indexes
    const fieldIndexes = {}
    if (table.tHead) {
        for (const [i, th] of table.tHead.querySelectorAll('th').entries()) {
            const field = th.dataset.field
            if (field) {
                fieldIndexes[field] = i
            }
            if (columns.length < i+1) {
                columns.push({})
            }
        }
    }

    for (const column of columns) {
        if (column.sortable === undefined) {
            column.sortable = true
        }
    }

    if (fields) {
        for (const [field, column] of Object.entries(fields)) {
            const fieldIndex = fieldIndexes[field]
            if (fieldIndex === undefined) {
                console.error(`${tableId}: ignore column configuration for field "${field}": field not found in thead`)
                continue
            }
            columns[fieldIndex] = {...columns[fieldIndex], ...column}
        }
    }

    return $(`#${tableId}`).bootstrapTable({columns, ...options})
}

/**
 * Initialize dirty state management for a form.
 * 
 * @param {string} formSelector
 */
function initDirty(formSelector) {
    const form = document.querySelector(formSelector)
    const buttons = form.querySelectorAll('button[type="submit"], button[type="reset"]')
    buttons.forEach(button => button.disabled = true)

    form.addEventListener('reset', ev => {
        $(form).dirty("refreshEvents")
    })

    $(form).dirty({
        preventLeaving: true,
        onDirty() {
            buttons.forEach(button => button.disabled = false)
        },
        onClean() {
            buttons.forEach(button => button.disabled = true)
        },
    })
}

/**
 * Initialize select2.
 * 
 * @param {string} selectSelector
 */
function initSelect2(selectSelector, {url, tags, ...options} = {}) {
    if (options.theme === undefined) {
        options.theme = 'bootstrap-5'
        options.width = '100%'
    }

    if (options.allowClear == undefined) {
        options.allowClear = true
        options.placeholder = ''
    }

    if (url) {
        options.ajax = {
            url,
            data(params) {
                return {
                    q: params.q,
                    page: params.page,
                }
            },
        }
    }
    
    options.tags = tags  // if True, allow free text responses

    $(selectSelector).select2(options) 
}

/**
 * Start a websocket.
 * @param {string} url URL of the websocket.
 * @param {object} options
 * @param {function} options.onMessage A function to call when a message is received from the websocket.
 * @param {boolean} options.reconnectButton If true, add a "Try to reconnect" button when connection to server is closed.
 * @param {string} options.name Optional name to display in debug messages.
 */
function startWebsocket(url, {onMessage, reconnectButton, name} = {}) {
    let websocket = new WebSocket(url)
    const prefix = name ? `${name} ` : ''

    websocket.onopen = (ev) => {
        if (DEBUG) {
            console.log(`${prefix}websocket: open`)
        }
    }

    websocket.onclose = (ev) => {
        if (DEBUG) {
            console.log(`${prefix}websocket: close`, ev.code)
        }

        websocket = null
        let msg = gettext("Connection to web server closed")
        if (ev.code == 3000) { // unauthorized
            msg += gettext(":") + " " + gettext("Unauthorized") + "."
            messages.error(msg)
        }
        else if (ev.code == 4181) { // celery_broker_not_connected
            msg += gettext(":") + " " + gettext("Celery broker is not connected") + "."
            messages.error(msg)
        }
        else {
            if (reconnectButton) {
                let bsAlert = null
                const messageElement = messages.error(`${msg}. <a href="#" class="reconnect">${gettext("Try to reconnect")}</a>.`)
                messageElement.querySelector('.reconnect').addEventListener('click', (ev) => {
                    ev.preventDefault()
                    startWebsocket(url, {onMessage, reconnectButton, name})
                    if (bsAlert && bsAlert._element) {
                        bsAlert.close()
                    }
                })
                bsAlert = new bootstrap.Alert(messageElement)
            }
            else {
                messages.error(`${msg}.`)
            }
        }
    }
    
    if (DEBUG || onMessage) {
        websocket.onmessage = (ev) => {
            const data = JSON.parse(ev.data)
            if (DEBUG) {
                console.log(`${prefix}websocket: message`, data)
            }
    
            onMessage(data)
        }
    }

    websocket.onerror = (ev) => {
        if (DEBUG) {
            console.error(`${prefix}websocket: error`, ev)
        }
        // No need to display error: onclosed is also automatically called
    }
}

function calculateDuration(start, end) {
    if (! start || start == 'null') {
        return null
    }
    else if (typeof(start.getMonth) != 'function') {
        start = new Date(start)
    }

    if (! end || end == 'null') {
        end = new Date()
    }
    else if (typeof(end.getMonth) != 'function') {
        end = new Date(end)
    }
    
    const total_ms = end - start
    const sign = total_ms < 0 ? '-' : ''
    const total_sec = Math.round(Math.abs(total_ms / 1000))
    const total_min = Math.floor(total_sec / 60)
    const remaining_sec = total_sec - 60 * total_min
    const total_h = Math.floor(total_min / 60)
    const remaining_min = total_min - 60 * total_h
    const total_j = Math.floor(total_h / 24)
    const remaining_h = total_h - 24 * total_j
    return `${sign}${total_j > 0 ? `${total_j}j&nbsp;` : ''}${remaining_h < 10 ? '0' : ''}${remaining_h}:${remaining_min < 10 ? '0' : ''}${remaining_min}:${remaining_sec < 10 ? '0' : ''}${remaining_sec}`
}

/**
 * Create a websocket to monitor the status of a task.
 * @param {HTMLElement} container
 */
function startTaskDetailWebsocket(container) {
    const task_id = container.dataset.taskId

    const id_elem = container.querySelector('[data-field="id"]')
    const name_elem = container.querySelector('[data-field="name"]')
    const params_elem = container.querySelector('[data-field="params"]')
    const worker_elem = container.querySelector('[data-field="worker"]')
    const state_elem = container.querySelector('[data-field="state"]')
    const progress_elem = container.querySelector('[data-field="progress"]')
    const details_elem = container.querySelector('[data-field="details"]')
    const start_elem = container.querySelector('[data-field="start"]')
    const end_elem = container.querySelector('[data-field="end"]')
    const duration_elem = container.querySelector('[data-field="duration"]')

    function onMessage(data) {
        if (id_elem) {
            id_elem.innerHTML = data.task.id ?? '-'
        }
        if (name_elem) {
            name_elem.innerHTML = data.task.name ?? '-'
        }
        if (params_elem) {
            params_elem.innerHTML = data.task.params ?? '-'
        }
        if (worker_elem) {
            worker_elem.innerHTML = data.task.worker ?? '-'
        }
        if (state_elem) {
            state_elem.innerHTML = taskFormatters.state(data.task.state) ?? '-'
        }
        if (progress_elem) {
            progress_elem.innerHTML = taskFormatters.progress(data.task.progress, {state: data.task.state}) ?? '-'
        }
        if (details_elem) {
            details_elem.innerHTML = data.task.details ?? '-'
        }
        if (start_elem) {
            start_elem.dataset.value = data.task.start
            start_elem.innerHTML = date_formatter(data.task.start) ?? '-'
        }
        if (end_elem) {
            end_elem.dataset.value = data.task.end
            end_elem.innerHTML = date_formatter(data.task.end) ?? '-'
        }
        if (duration_elem) {
            duration_elem.innerHTML = taskFormatters.duration(null, {start: data.task.start, end: data.task.end}) ?? '-'
        }
    }
    
    function updateTaskDuration() {
        setTimeout(() => {
            duration_elem.innerHTML = calculateDuration(start_elem.dataset.value, end_elem.dataset.value) ?? '-'
            updateTaskDuration()
        }, 900)
    }
    
    const url = `${WEBSOCKET_PREFIX}/ws/task/${task_id}/`
    startWebsocket(url, {onMessage, name: `task-${task_id}`})
    if (duration_elem) {
        updateTaskDuration()
    }
}

// Attach "submit-on-change" events
for (const _element of document.querySelectorAll('.submit-on-change')) {
    _element.addEventListener('change', ev => ev.target.form.submit())
}
