from palm.palm import ProtoBase, is_string, RepeatedSequence, ProtoValueError

_PB_type = type
_PB_finalizers = []


class Request(ProtoBase):
    _required = [1]
    _field_map = {'payload': 1}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['payload']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_payload(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, ProtoBase.TYPE_string, 'payload')
            self._cache[1] = r
        return r

    def _establish_parentage_payload(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_payload), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_payload
                v._pbf_establish_parent_callback = self._establish_parentage_payload

    def _set_payload(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_payload(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field payload"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = ProtoBase.TYPE_string

    def _mod_payload(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = ProtoBase.TYPE_string

    def _del_payload(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "payload"

    payload = property(_get_payload, _set_payload, _del_payload)

    @property
    def payload__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def payload__type(self):
        return ProtoBase.TYPE_string

    def _finalize_payload(cls):
        if is_string(ProtoBase.TYPE_string):
            cls._pbf_strings.append(1)
        elif _PB_type(ProtoBase.TYPE_string) is _PB_type:
            assert issubclass(ProtoBase.TYPE_string, RepeatedSequence)
            if is_string(ProtoBase.TYPE_string.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_payload)


TYPE_Request = Request
_PB_finalizers.append('Request')


for cname in _PB_finalizers:
    eval(cname)._pbf_finalize()

del _PB_finalizers
