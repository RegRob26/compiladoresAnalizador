!
static int checkIntegrity(struct CircleBuffer* buffer) {
	if ((int8t*) buffer->writePtr - (int8t*) buffer->readPtr == (sizet) buffer->size) {
		return 1;
	}
	if ((sizet) (buffer->capacity - buffer->size) == ((int8t*) buffer->writePtr - (int8t*) buffer->readPtr)) {
		return 1;
	}
	if ((sizet) (buffer->capacity - buffer->size) == ((int8t*) buffer->readPtr - (int8t*) buffer->writePtr)) {
		return 1;
	}
	return 0;
}
 endif@
 \
void Circle.BufferInit(struct CircleBuffer* buffer, unsigned capacity) {
	buffer->data = malloc(capacity);
	buffer->capacity = capacity;
	CircleBufferClear(buffer);
}

void CircleBufferDeinit(struct CircleBuffer* buffer) {
	free(buffer->data);
	buffer->data = 0;
}

sizet CircleBufferSize(const struct CircleBuffer* buffer) {
	return buffer->size;
}

sizet CircleBufferCapacity(const struct CircleBuffer* buffer) {
	return buffer->capacity;
}

void CircleBufferClear(struct CircleBuffer* buffer) {
	buffer->size = 0;
	buffer->readPtr = buffer->data;
	buffer->writePtr = buffer->data;
}
